# encoding:utf-8
import time
from celery.task import task
from ftpConnection import MYFTP
from image_talk import neural_talk

import redis

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

# start redis server
#r = redis.StrictRedis(**config)
r = redis.Redis(**config)

 
# hostaddr = '192.168.112.74' # windows ftp地址
hostaddr = '172.16.6.157' # linux ftp地址
username = 'mediaftp' # 用户名
password = 'medialab313' # 密码
port  =  21   # 端口号 
# rootdir_local  = 'D:/Work/testFiles/' #linux  本地目录
rootdir_local  = '/home/medialab/deploy/imagecache/' #linux  本地目录
rootdir_remote = '/'          # 远程目录

@task
def imageRecognition(afterFilename,filename,csrfvar):
    # do the work
    f = MYFTP(hostaddr, username, password, rootdir_remote, port)
    f.login()
    print (rootdir_local+afterFilename+" ; "+rootdir_remote+afterFilename)
    f.download_file(rootdir_local+afterFilename, rootdir_remote+afterFilename)
    description = neural_talk(rootdir_local+afterFilename)
#     description = "this is a result"

    # notify Node.js that the job has finished
    topic = "JOB_FINISH"
    r.publish(topic, csrfvar+";"+str(filename)+": " +description)
    
    