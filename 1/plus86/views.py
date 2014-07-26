# Create your views here.
#! /usr/bin/env python
# coding=utf-8
from django.http import HttpResponse

import hashlib
import xml.etree.ElementTree as ET
import urllib2
# import requests
import json
 
 

def checkSignature(request):
    token = "zhouchaoweixin"
    signature = request.GET.get('signature', None)  
    timestamp = request.GET.get('timestamp', None)
    nonce = request.GET.get('nonce', None)
    echostr = request.GET.get('echostr', None)
    tmpList = [token, timestamp, nonce]
    tmpList.sort()
    tmpstr = "%s%s%s" % tuple(tmpList)
    hashstr = hashlib.sha1(tmpstr).hexdigest()
    # return "echostr: %s" % echostr
    if hashstr == signature:
        return HttpResponse(echostr)
    else:
        return HttpResponse("")
 
 
