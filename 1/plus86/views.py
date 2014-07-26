# -*- coding: utf-8 -*-
# Create your views here.
#! /usr/bin/env python

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.template import RequestContext, Template
from django.utils.encoding import smart_str, smart_unicode


import hashlib
import xml.etree.ElementTree as ET
import urllib2,urllib,time
# import requests
import json
 
 
def paraseMsgXml(rootElem):  
    msg = {}  
    if rootElem.tag == 'xml':  
        for child in rootElem:  
            msg[child.tag] = smart_str(child.text)  
    return msg  

def responseMsg(request):
    rawStr = smart_str(request.raw_post_data)  
    #rawStr = smart_str(request.POST['XML'])  
    msg = paraseMsgXml(ET.fromstring(rawStr))
    textTpl = """<xml>
             <ToUserName><![CDATA[%s]]></ToUserName>
             <FromUserName><![CDATA[%s]]></FromUserName>
             <CreateTime>%s</CreateTime>
             <MsgType><![CDATA[%s]]></MsgType>
             <Content><![CDATA[%s]]></Content>
             <FuncFlag>0</FuncFlag>
             </xml>"""
    Content = 'zhouchao'
 
    # if Content is not False:
    echostr = textTpl % (msg['FromUserName'], msg['ToUserName'], str(int(time.time())), 'text', Content)
    fileHandle = open('log.log', 'w')
    fileHandle.write (echostr)
    fileHandle.close()
    return echostr
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
    # return "echostr: %s" % echostr
    if hashstr == signature:
        return echostr
    else:
        return None
 

def handleRequest(request):  
    if request.method == 'GET':  
        #response = HttpResponse(request.GET['echostr'],content_type="text/plain")  
        response = HttpResponse(checkSignature(request),content_type="text/plain")  
        return response  
    elif request.method == 'POST':  
        #c = RequestContext(request,{'result':responseMsg(request)})  
        #t = Template('{{result}}')  
        #response = HttpResponse(t.render(c),content_type="application/xml")  
        response = HttpResponse(responseMsg(request),content_type="application/xml")  
        return response  
    else:  
        return None  


def paraseYouDaoXml(rootElem):  
    replyContent = ''  
    if rootElem.tag == 'youdao-fanyi':  
        for child in rootElem:  
             
            if child.tag == 'errorCode':  
                if child.text == '20':  
                    return 'too long to translate\n'  
                elif child.text == '30':  
                    return 'can not be able to translate with effect\n'  
                elif child.text == '40':  
                    return 'can not be able to support this language\n'  
                elif child.text == '50':  
                    return 'invalid key\n'  
  
            
            elif child.tag == 'query':  
                replyContent = "%s%s\n" % (replyContent, child.text)  
  
              
            elif child.tag == 'translation':   
                replyContent = '%s%s\n%s\n' % (replyContent, '-' * 3 + u'有道翻译' + '-' * 3, child[0].text)  
  
             
            elif child.tag == 'basic':   
                replyContent = "%s%s\n" % (replyContent, '-' * 3 + u'基本词典' + '-' * 3)  
                for c in child:  
                    if c.tag == 'phonetic':  
                        replyContent = '%s%s\n' % (replyContent, c.text)  
                    elif c.tag == 'explains':  
                        for ex in c.findall('ex'):  
                            replyContent = '%s%s\n' % (replyContent, ex.text)  
  
             
            elif child.tag == 'web':   
                replyContent = "%s%s\n" % (replyContent, '-' * 3 + u'网络释义' + '-' * 3)  
                for explain in child.findall('explain'):  
                    for key in explain.findall('key'):  
                        replyContent = '%s%s\n' % (replyContent, key.text)  
                    for value in explain.findall('value'):  
                        for ex in value.findall('ex'):  
                            replyContent = '%s%s\n' % (replyContent, ex.text)  
                    replyContent = '%s%s\n' % (replyContent,'--')  
    return replyContent  
  
