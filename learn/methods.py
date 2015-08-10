
#-*- coding:utf-8 -*-
'''
Created on 2015年7月22日

@author: Zhangxusheng
'''
import uuid
from tasks import image_recognition

def handleUploadedFile(files):

    images = []
    for f in files:
        print(f.name)
        unique_id = str(uuid.uuid1()).replace('-','')
        file_ext  = f.name.split('.')[-1]
        filename  = '.'.join([unique_id, file_ext])
        print(filename)       
#        dst_file  = ''.join(['D:/Work/UploadFiles/', filename])
        dst_file  = ''.join(['/home/medialab/ftpfolder/', filename])
        with open(dst_file, 'wb+') as fd:
            for chunk in f.chunks():
                fd.write(chunk)
  
        images.append([filename, f.name])
    image_recognition.delay(images)
  
    return unique_id
