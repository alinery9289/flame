# encoding:utf-8
import time
import uuid
from celery.task import task
from ftpConnection import MYFTP
from ImageTalk import neural_talk

import redis
import os
import shutil
#----------------------------------------------------------------------
#           start Redis client for publishing messages
#----------------------------------------------------------------------
config = {
#         'host': '0.0.0.0', # accpet any connections
        'host': '172.16.6.157', # Redis server address
        'port': 6379,
        'password': 123456,
        'db': 0,
        }

# start redis client
#r = redis.StrictRedis(**config)
r = redis.Redis(**config)


hostaddr = '172.16.6.157'
username = 'mediaftp'
password = 'medialab313'
port  =  21
rootdir_local  = '/home/medialab/deploy/imagecache/'
rootdir_remote = '/home/medialab/ftpfolder'
#rootdir_remote = ''


@task
def image_recognition(images):
    """
    @param images - list of image files to be processed on remote ftp server,
           consists of [filename, org_filename] entries, where org_filename
           is the name when the image is uploaded
    @param csrfvar
    """
    # do the work
    f = MYFTP(hostaddr, username, password, rootdir_remote, port)
    f.login()

    unique_id = str(uuid.uuid1()).replace('-','')
    work_dir = ''.join([rootdir_local, unique_id])
    os.mkdir(work_dir)

    files = []
    for img in images:
        filename, org_filename = img
        print(filename, org_filename)

        src_file = '/'.join([rootdir_remote, filename])
        dst_file = '/'.join([work_dir, filename])
        print ("src %s, dst %s" % (src_file, dst_file))
        f.download_file(dst_file, src_file)
        files.append(filename)

    descriptions = neural_talk(work_dir, files)

    # apped result to redis db
    session_id = filename.split('.')[0]
    for score, name in zip(range(1, len(descriptions)+1), descriptions):
        print(name, str(score))
        r.zadd(session_id, name, score)

    shutil.rmtree(work_dir)
