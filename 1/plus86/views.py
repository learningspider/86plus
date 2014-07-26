# Create your views here.
#! /usr/bin/env python
# coding=utf-8
from django.http import HttpResponse

import hashlib
import xml.etree.ElementTree as ET
import urllib2
# import requests
import json
 
 
def parse_msg():
    recvmsg = request.body.read()
    root = ET.fromstring(recvmsg)
    msg = {}
    for child in root:
        msg[child.tag] = child.text
    return msg

def response_msg():
    msg = parse_msg()
    textTpl = """<xml>
             <ToUserName><![CDATA[%s]]></ToUserName>
             <FromUserName><![CDATA[%s]]></FromUserName>
             <CreateTime>%s</CreateTime>
             <MsgType><![CDATA[%s]]></MsgType>
             <Content><![CDATA[%s]]></Content>
             <FuncFlag>0</FuncFlag>
             </xml>"""
    Content = "zhouchao"
 
    # if Content is not False:
    echostr = textTpl % (msg['FromUserName'], msg['ToUserName'], str(int(time.time())), msg['MsgType'], Content)
    return HttpResponse(echostr)
    # else:
    #     echostr = textTpl % (msg['FromUserName'], msg['ToUserName'], str(int(time.time())), msg['MsgType'], "Content")
    #     return echostr

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
    if request.method == 'POST':
        response_msg()
    # return "echostr: %s" % echostr
    if hashstr == signature:
        return HttpResponse(echostr)
    else:
        return HttpResponse("")
 
 
