# -*- coding: utf8 -*-


#!/usr/bin/env python

import sys 
reload(sys) 
sys.setdefaultencoding('utf8')
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.template import RequestContext, Template
from django.utils.encoding import smart_str, smart_unicode
from django.shortcuts import render_to_response


import hashlib
import xml.etree.ElementTree as ET
import urllib2,urllib,time
import json
from plus86.models import memberCard

# import requests




def responseMsg(request):
    recvmsg = smart_str(request.raw_post_data)
    root = ET.fromstring(recvmsg)
    msg={}
    
    for child in root:
        msg[child.tag] = child.text
    #request.session["fromusername"] = msg[FromUserName]
    
                
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
    textTp6 = """<xml>
                <ToUserName><![CDATA[%s]]></ToUserName>
                <FromUserName><![CDATA[%s]]></FromUserName>
                <CreateTime>%s</CreateTime>
                <MsgType><![CDATA[news]]></MsgType>
                <ArticleCount>1</ArticleCount>
                <Articles>
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
    openid= msg['FromUserName']
    ''' msgt=msg['MsgTpye']
    if msgt=='text':
        echostr = textTpl % (msg['FromUserName'], msg['ToUserName'], str(int(time.time())), Title1, De1, pic1, url1, msg['MsgType'], De2, pic2, url2, Title3, De3, pic3, url3)
    else:
        echostr = textTpl % (msg['FromUserName'], msg['ToUserName'], str(int(time.time())), Title1, De1, pic1, url1, msg['MsgType'], De2, pic2, url2, Title3, De3, pic3, url3)
        if msg['Event']=='CLICK':
            if msg['EventKey']=='V1001_GOOD':
                #try:
                    #user=memberCard.objects.filter(openid=fromusername)
                echostr = textTp6 % (msg['FromUserName'], msg['ToUserName'], str(int(time.time())), Title1, De1, pic1, url1)
                #'http://86plus.sinaapp.com/registor?openid='+openid
                except DoesNotExist:
                    echostr = textTpl % (msg['FromUserName'], msg['ToUserName'], str(int(time.time())), '申请会员卡', '申请会员卡',url1, 'http://86plus.sinaapp.com/registor?openid='+openid)
                    return echostr
                except MultipleObjectsReturned:
                    return render_to_response('404.html')'''
    echostr = textTpl % (msg['FromUserName'], msg['ToUserName'], str(int(time.time())), Title1, De1, pic1, url1, msg['MsgType'], De2, pic2, url2, Title3, De3, pic3, url3)

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

def creatmenu(request):
    appid="wx5346a6f59b5e4dd8"
    secret="3079a01e4c7b9b61da0cbf7808047d7c"
    url='https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid='+appid+'&secret='+secret
    response = urllib2.urlopen(url)
    html = response.read()
    tokeninfo = json.loads(html)
    token=tokeninfo['access_token']
    post='''
 {
     "button":[
     {	
          "type":"click",
          "name":"搜索",
           "sub_button":[
           {	
               "type":"view",
               "name":"搜索",
               "url":"http://www.soso.com/"
            },
            {
               "type":"view",
               "name":"视频",
               "url":"http://v.qq.com/"
            },
            {
               "type":"click",
               "name":"赞一下我们",
               "key":"V1001_GOOD6"
            }]
      },
      {
           "type":"click",
           "name":"百度搜索",
           "sub_button":[
           {	
               "type":"view",
               "name":"搜索",
               "url":"http://www.baidu.com/"
            },
            {
               "type":"view",
               "name":"视频",
               "url":"http://v.qq.com/"
            },
            {
               "type":"click",
               "name":"赞一下我们",
               "key":"V1001_GOOD5"
            }]
      },
      {
           "name":"会员",
           "sub_button":[
           {
               "type":"click",
               "name":"会员卡",
               "key":"V1001_GOOD"
            },
            {
               "type":"click",
               "name":"赞一下我们",
               "key":"V1009_GOOD"
            }]
       }]
 }'''
    url = 'https://api.weixin.qq.com/cgi-bin/menu/create?access_token='+token
    req = urllib2.Request(url, post)
    response = urllib2.urlopen(req)
    return response


def deletemenu(request):
    appid="wx5346a6f59b5e4dd8"
    secret="3079a01e4c7b9b61da0cbf7808047d7c"
    url='https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid='+appid+'&secret='+secret
    response = urllib2.urlopen(url)
    html = response.read()
    tokeninfo = json.loads(html)
    token=tokeninfo['access_token']       
    url = 'https://api.weixin.qq.com/cgi-bin/menu/delete?access_token='+token
    req = urllib2.Request(url)
    response = urllib2.urlopen(req)
    return response
 
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

def membercard(request):
    
    return render_to_response('index2.html')

def register(request):
    return render_to_response('register.html')
	
def registercheck(request):
    idname = request.POST.get( 'username', '' )
    email = request.POST.get( 'email', '' )
    phonenum = request.POST.get( 'phonenum', '' )
    openid = request.POST.get( 'ExPws', '' )
    p = Publisher(openid=openid,
         phonenumber=phonenum,
         name=email,
         IDcard=idname)
    p.save()
    return render_to_response('index2.html')

def checkmember(request):
    #fromusername=request.session.get('fromusername',None)
    try:
        user=1
        #user=memberCard.objects.get(openid=fromusername)
    except DoesNotExist:
        return render_to_response('register.html')
    except MultipleObjectsReturned:
        return render_to_response('404.html')
    return render_to_response('404.html')
  
