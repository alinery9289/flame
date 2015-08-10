#-*- coding:utf-8 -*-

from django.shortcuts import *
from django.http import *
from learn.forms import *
from models import *
from methods import *

import json
import uuid
import redis

config = {
        'host': '172.16.6.157', # Redis server address
        'port': 6379,
        'password': 123456,
        'db': 0,
        }

# start redis server
#r = redis.StrictRedis(**config)
r = redis.Redis(**config)

def home(request):
    return render(request, 'home.html')

def userProc(request):
    if request.method == 'POST':# 当提交表单时

        form = AddUserForm(request.POST) # form 包含提交的数据

        if form.is_valid():# 如果提交的数据合法
            authcode1=str(uuid.uuid1()).replace('-','')
            username1 =str( form.cleaned_data['username'])
            password1 = str( form.cleaned_data['password1'])
            password2 = str( form.cleaned_data['password2'])
            email1 = str( form.cleaned_data['email'])
            #print authcode1+" "+username1+" "+password1+" "+email1
            if password1==password2:
                oneUser = user(authcode=authcode1,userid=username1,
                        password=password1,email=email1,
                        userstorage=500*1000*1000)
                oneUser.save()
                return HttpResponse('Save ok!')
            else : return HttpResponse('Error: The two password are different!')
        else: return HttpResponse('Error: Can\'t save!')

def mediaFileProc(request):
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            mySession=handleUploadedFile(request.FILES.getlist("fileList"))
            return HttpResponse(mySession)
    return render_to_response("Error")

def getImageRec(request,imageId):
    if request.method == 'GET':
        talk_word=r.zrange(imageId, 0, -1)
        if talk_word== []:
            return HttpResponse("Processing")
        else :
            r.zremrangebyrank(imageId, 0, -1)
            return HttpResponse(talk_word)
    return render_to_response("Error")

def testJson(request,question,value1):
    if request.method == 'GET' :
        response_data = {}
        response_data['result'] = question
        response_data['1'] = value1
        return HttpResponse(json.dumps(response_data), content_type="application/json")
