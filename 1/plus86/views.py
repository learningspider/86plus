# -*- coding: utf-8 -*-
#!/usr/bin/env python

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.template import RequestContext, Template
from django.utils.encoding import smart_str, smart_unicode


import hashlib
import xml.etree.ElementTree as ET
import urllib2,urllib,time
# import requests

 
 


def responseMsg(request):
    recvmsg = smart_str(request.raw_post_data)
    root = ET.fromstring(recvmsg)
    msg = {}
    for child in root:
        msg[child.tag] = child.text
    #textTpl = "<xml><ToUserName><![CDATA[%s]]></ToUserName><FromUserName><![CDATA[%s]]></FromUserName><CreateTime>%s</CreateTime><MsgType><![CDATA[%s]]></MsgType><Content><![CDATA[%s]]></Content><FuncFlag>0</FuncFlag></xml>"
    textTpl = """<xml>
                <ToUserName><![CDATA[%s]]></ToUserName>
                <FromUserName><![CDATA[%s]]></FromUserName>
                <CreateTime>%s</CreateTime>
                <MsgType><![CDATA[news]]></MsgType>
                <ArticleCount>3</ArticleCount>
                <Articles>
                <item>
                <Title><![CDATA[%s]]></Title> 
                <Description><![CDATA[%s]]></Description>
                <PicUrl><![CDATA[%s]]></PicUrl>
                <Url><![CDATA[%s]]></Url>
                </item>
                <item>
                <Title><![CDATA[%s]]></Title>
                <Description><![CDATA[%s]]></Description>
                <PicUrl><![CDATA[%s]]></PicUrl>
                <Url><![CDATA[%s]]></Url>
                </item>
                <item>
                <Title><![CDATA[%s]]></Title>
                <Description><![CDATA[%s]]></Description>
                <PicUrl><![CDATA[%s]]></PicUrl>
                <Url><![CDATA[%s]]></Url>
                </item>
                </Articles>
                </xml> """
    Title1 = u'华北黄淮等地将一口气热到月底'
    Title2 = u'河南6月来降水偏少6成 近半地区现重旱级气象干旱'
    Title3 = u'杭州风雨晚来急 1小时降下90毫米雨'
    De1 = u'华北黄淮等地将一口气热到月底!'
    De2 = u'河南6月来降水偏少6成 近半地区现重旱级气象干旱!'
    De3 = u'杭州风雨晚来急 1小时降下90毫米雨!'
    pic1 = 'http://i.weather.com.cn/images/cn/news/2014/07/26/814284E37EF400D973A7A81C5BBE627A.jpg'
    pic2 = 'http://i.weather.com.cn/images/cn/news/2014/07/26/7FBDABDBAECFE8395DCC4B7C6CEAFF5D.jpg'
    pic3 = 'http://i.weather.com.cn/images/cn/news/2014/07/26/85A6D03788AE64849402ABE5E28CE78E.jpg'
    url1 = 'http://news.weather.com.cn/2014/07/2164829.shtml'
    url2 = 'http://news.weather.com.cn/2014/07/2164872.shtml'
    url3 = 'http://news.weather.com.cn/2014/07/2164877.shtml'
    echostr = textTpl % (msg['FromUserName'], msg['ToUserName'], str(int(time.time())), Title1, De1, pic1, url1, Title2, De2, pic2, url2, Title3, De3, pic3, url3)
    return echostr
   

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
 
@csrf_exempt 
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



  
