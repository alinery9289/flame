#-*- coding:utf-8 -*-
'''
Created on 2015.7.21

@author: Zhangxusheng
'''

from django import forms
 
class AddUserForm(forms.Form):
    username = forms.CharField()
    password1 = forms.CharField()
    password2 = forms.CharField()
    email = forms.CharField()
    
class UploadForm(forms.Form):
    fileList = forms.FileField()