
#-*- coding:utf-8 -*-
'''
Created on 2015年7月22日

@author: Zhangxusheng
'''
import uuid
from tasks import *

def handleUploadedFile(files,csrfvar):
    for f in files:      
        fileid=str(uuid.uuid1()).replace('-','')
        destination = open('/home/medialab/ftpfolder' +fileid+'_'+ f.name,'wb+')
        for chunk in f.chunks(): 
            destination.write(chunk)
        destination.close()
        imageRecognition.delay(fileid+'_'+ f.name,f.name,csrfvar)