# -*- coding: utf8 -*-


#!/usr/bin/env python

import sys 
reload(sys) 
sys.setdefaultencoding('utf8')
from django.http import HttpResponse,HttpResponseRedirect
from itertools import chain
from django.views.decorators.csrf import csrf_exempt
from django.template import RequestContext, Template
from django.utils.encoding import smart_str, smart_unicode
from django.shortcuts import render_to_response,render
from django.contrib.sessions.models import Session
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User

import hashlib
import re
import xml.etree.ElementTree as ET
import urllib2,urllib,time
import json
from plus86.models import memberCard,UserProfile,clothes
from plus86.models import user as userlogin6


# import requests




def responseMsg(request):
    recvmsg = smart_str(request.raw_post_data)
    root = ET.fromstring(recvmsg)
    msg={}
    
    for child in root:
        msg[child.tag] = child.text
    '''if 'openid' in request.session:
        print request.session["openid"]
    else:
        request.session['openid'] = msg['FromUserName']'''
        
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
    text1='''<xml>
             <ToUserName><![CDATA[%s]]></ToUserName>
             <FromUserName><![CDATA[%s]]></FromUserName>
             <CreateTime>%s</CreateTime>
             <MsgType><![CDATA[text]]></MsgType>
             <Content><![CDATA[%s]]></Content>
             </xml>'''
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
    MsgType=msg['MsgType']
    if MsgType=="text":
        if msg['Content']=='登录':
            echostr = text1 % (msg['FromUserName'], msg['ToUserName'], str(int(time.time())),'<a href="https://open.weixin.qq.com/connect/oauth2/authorize?appid=wx5346a6f59b5e4dd8&redirect_uri=http://86plus.sinaapp.com/checkweixininfo/&response_type=code&scope=snsapi_userinfo&state=123#wechat_redirect">OAUTH登录</a>')
        elif msg['Content']=='查询商品':
            echostr = text1 % (msg['FromUserName'], msg['ToUserName'], str(int(time.time())),'<a href="http://86plus.vipsinaapp.com/queryproductstatus/">查询所有商品</a>')
        elif msg['Content']=='隐藏':
            echostr = text1 % (msg['FromUserName'], msg['ToUserName'], str(int(time.time())),'<a href="http://86plus.vipsinaapp.com/yincang/">隐藏测试</a>')    
        else:
            echostr = textTpl % (msg['FromUserName'], msg['ToUserName'], str(int(time.time())), Title1, De1, pic1, url1, MsgType, De2, pic2, url2, Title3, De3, pic3, url3)
    elif MsgType=="event":
        if msg['Event']=="CLICK":
            if msg['EventKey']=="V1001_GOOD":
                u1=memberCard.objects.filter(openid=msg['FromUserName'])
                if len(u1)==0:
                #request.session['fromusername'] = msg[FromUserName]
                    echostr = textTp6 % (msg['FromUserName'], msg['ToUserName'], str(int(time.time())), '申请会员卡', '申请会员卡', 'http://86plus.vipsinaapp.com/site_media/img/companylogo.png', 'http://86plus.sinaapp.com/register?openid='+openid)
                else:
                    echostr = textTp6 % (msg['FromUserName'], msg['ToUserName'], str(int(time.time())), '会员卡', '点击图片查看会员卡', 'http://86plus.vipsinaapp.com/site_media/img/companylogo.png', 'http://86plus.sinaapp.com/membercard?openid='+openid)
            elif msg['EventKey']=="V1006000_GOOD": 
                echostr = text1 % (msg['FromUserName'], msg['ToUserName'], str(int(time.time())),'<a href="https://open.weixin.qq.com/connect/oauth2/authorize?appid=wx5346a6f59b5e4dd8&redirect_uri=http://86plus.sinaapp.com/checkweixininfo&response_type=code&scope=snsapi_base&state=123#wechat_redirect">OAUTH登录</a>')
        elif  msg['Event']=="subscribe":
            #echostr = text1 % (msg['FromUserName'], msg['ToUserName'], str(int(time.time())),'关注86plus,关注生活')
            echostr = textTp6 % (msg['FromUserName'], msg['ToUserName'], str(int(time.time())), '谢谢关注', '点击图片查看功能介绍', 'http://86plus.vipsinaapp.com/site_media/img/companylogo.png', 'http://86plus.sinaapp.com/welcome/')
    #echostr = textTpl % (msg['FromUserName'], msg['ToUserName'], str(int(time.time())), Title1, De1, pic1, url1, MsgType, De2, pic2, url2, Title3, De3, pic3, url3)

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
          "name":"精彩导航",
           "sub_button":[
           {	
               "type":"view",
               "name":"86PLUS公益",
               "url":"http://86plus.sinaapp.com/gongyi/"
            },
            {
               "type":"view",
               "name":"美食博览",
               "url":"http://v.qq.com/"
            },
            {
               "type":"view",
               "name":"服饰聚焦",
               "url":"http://86plus.sinaapp.com/productfushi/beijing/1/"
            },
            {
               "type":"view",
               "name":"86PLUS介绍",
               "url":"http://86plus.sinaapp.com/welcome/"
            }]
      },
      {
           "type":"click",
           "name":"活动公告",
           "sub_button":[
           {	
               "type":"view",
               "name":"招商加盟",
               "url":"http://www.baidu.com/"
            },
            {
               "type":"view",
               "name":"支付教学",
               "url":"http://v.qq.com/"
            },
            {
               "type":"view",
               "name":"活动资讯",
               "url":"http://v.qq.com/"
            },
            {
               "type":"click",
               "name":"86Plus公告",
               "key":"V1001_GOOD5"
            }]
      },
      {
           "name":"会员地带",
           "sub_button":[
           {
               "type":"view",
               "name":"刮刮卡",
               "url":"http://86plus.vipsinaapp.com/guaguaka/"
            },
           {
               "type":"click",
               "name":"会员卡",
               "key":"V1001_GOOD"
            },
            {
               "type":"view",
               "name":"注册",
               "url":"http://86plus.vipsinaapp.com/userregister/"
            },
            {
               "type":"view",
               "name":"普通登录",
               "url":"http://86plus.vipsinaapp.com/userlogin/"
            },
            {
               "type":"view",
               "name":"Oauth登录",
               "url":"https://open.weixin.qq.com/connect/oauth2/authorize?appid=wx5346a6f59b5e4dd8&redirect_uri=http://86plus.sinaapp.com/checkweixininfo/&response_type=code&scope=snsapi_userinfo&state=123#wechat_redirect"
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
		
@csrf_exempt 
def membercard(request):
    if not request.user.is_authenticated():
            return HttpResponseRedirect('/userlogin/')
    #userinfo=request.user
    open = request.GET.get('openid', None)
    u1=memberCard.objects.filter(openid=open)
    for blog in list(u1):
        dic={}
        dic['openid']=str(blog.openid)
        dic['phonenumber']=str(blog.phonenumber)
        dic['email']=str(blog.name)
        dic['IDcard']=str(blog.IDcard)
        dic['username']=str(blog.username)
    return render_to_response('index2.html',{'u':dic})
    #return render_to_response('405.html',{'u':dic})


@csrf_exempt 
def register(request):
    openid = request.GET.get('openid', None)
    return render_to_response('register.html',{"openid":openid})
	
@csrf_exempt	
def reg(request):
    #if request.session['openid']:
    '''if "openid" in request.session:
        fromuser=request.session['openid']
    else:
        fromuser="zhou"'''
    idname = request.POST.get( 'IDcard', None )
    username = request.POST.get( 'username', None )
    email = request.POST.get( 'email', None)
    phonenum = request.POST.get( 'phonenumber', None)
    openid = request.POST.get( 'ExPws', None)
    '''if openid is None:
        return render_to_response('404_9.html')'''
    p = memberCard(openid=openid,
         phonenumber=phonenum,
         name=email,
         IDcard=idname,
         username=username)
    p.save()
    return render_to_response('index2.html')

def checkmember(request):
    #fromusername=request.session.get('fromusername',None)
    '''try:
        user=1
        #user=memberCard.objects.get(openid=fromusername)
    except DoesNotExist:
        return render_to_response('register.html')
    except MultipleObjectsReturned:
        return render_to_response('404_9.html')'''
    return render_to_response('404_9.html')

@csrf_exempt
def getweixininfo(request):
    '''pattern = re.compile(r'iPhone')
    match = pattern.search(request.META['HTTP_USER_AGENT'])
    if match:
        return render_to_response('404.html')'''
    codekey=request.GET.get('code', None)
    if codekey is None:
        return render_to_response('404_9.html')
    appid="wx5346a6f59b5e4dd8"
    secret="3079a01e4c7b9b61da0cbf7808047d7c"
    url='https://api.weixin.qq.com/sns/oauth2/access_token?appid='+appid+'&secret='+secret+'&code='+codekey+'&grant_type=authorization_code'
    response6 = urllib2.urlopen(url)
    html = response6.read()
    tokeninfo = json.loads(html)
    token=tokeninfo['access_token']
    openid=tokeninfo['openid']
    url = 'https://api.weixin.qq.com/sns/userinfo?access_token='+token+'&openid='+openid
    #request.encoding='gb2312'
    response1 = urllib2.urlopen(url)
    html1 = response1.read()
    userinfo = json.loads(html1)
    userlog=userlogin6.objects.filter(username=openid)
    user6=openid+'8'
    if len(userlog)==0:       
        u= userlogin6(username=openid,verify=user6)
        u.save()
        user1 = User.objects.create_user(openid, 'qiqi@86plus.net', user6)
        user1.save()
    user = authenticate(username=openid,password=user6)  
    if user is not None:
        if user.is_active:  
            login(request, user) 
            #return render(request,'405.html',{'res':request.META['HTTP_USER_AGENT']})   
            return render(request,'oauth2_openid.html',{'res':userinfo})     
    else:  
        #验证失败，暂时不做处理  
        return render_to_response('404_9.html')
    
  
  
def postrequest(request,postinfo,urlinfo):
    appid="wx5346a6f59b5e4dd8"
    secret="3079a01e4c7b9b61da0cbf7808047d7c"
    url='https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid='+appid+'&secret='+secret
    response = urllib2.urlopen(url)
    html = response.read()
    tokeninfo = json.loads(html)
    token=tokeninfo['access_token']
    url = urlinfo+token
    req = urllib2.Request(url, postinfo)
    response = urllib2.urlopen(req)
    return response 

def createproduct(request):
    postinfo='''{
    "product_base": {
        "category_id": [
            "537074298"
        ],
        "property": [
            {
                "id": "1075741879",
                "vid": "1079749967"
            },
            {
                "id": "1075754127",
                "vid": "1079795198"
            },
            {
                "id": "1075777334",
                "vid": "1079837440"
            }
        ],
        "name": "testaddproduct",
        "sku_info": [
            {
                "id": "1075741873",
                "vid": [
                    "1079742386",
                    "1079742363"
                ]
            }
        ],
        "main_img": "http://mmbiz.qpic.cn/mmbiz/4whpV1VZl2iccsvYbHvnphkyGtnvjD3ulEKogfsiaua49pvLfUS8Ym0GSYjViaLic0FD3vN0V8PILcibEGb2fPfEOmw/0", 
        "img": [
            "http://mmbiz.qpic.cn/mmbiz/4whpV1VZl2iccsvYbHvnphkyGtnvjD3ulEKogfsiaua49pvLfUS8Ym0GSYjViaLic0FD3vN0V8PILcibEGb2fPfEOmw/0"
        ],
        "detail": [
            {
                "text": "test first"
            },
            {
                "img": "http://mmbiz.qpic.cn/mmbiz/4whpV1VZl2iccsvYbHvnphkyGtnvjD3ul1UcLcwxrFdwTKYhH9Q5YZoCfX4Ncx655ZK6ibnlibCCErbKQtReySaVA/0"
            },
            {
                "text": "test again"
            }
        ],
        "buy_limit": 10
    },
    "sku_list": [
        {
            "sku_id": "1075741873:1079742386",
            "price": 30,
            "icon_url": "http://mmbiz.qpic.cn/mmbiz/4whpV1VZl28bJj62XgfHPibY3ORKicN1oJ4CcoIr4BMbfA8LqyyjzOZzqrOGz3f5KWq1QGP3fo6TOTSYD3TBQjuw/0",
            "product_code": "testing",
            "ori_price": 9000000,
            "quantity": 800
        },
        {
            "sku_id": "1075741873:1079742363",
            "price": 30,
            "icon_url": "http://mmbiz.qpic.cn/mmbiz/4whpV1VZl28bJj62XgfHPibY3ORKicN1oJ4CcoIr4BMbfA8LqyyjzOZzqrOGz3f5KWq1QGP3fo6TOTSYD3TBQjuw/0",
            "product_code": "testingtesting",
            "ori_price": 9000000,
            "quantity": 800
        }
    ],
    "attrext": {
        "location": {
            "country": "中国",
            "province": "广东省",
            "city": "广州市",
            "address": "T.I.T创意园"
        },
        "isPostFree": 0,
        "isHasReceipt": 1,
        "isUnderGuaranty": 0,
        "isSupportReplace": 0
    },
    "delivery_info": {
        "delivery_type": 0,
        "template_id": 0, 
        "express": [
            {
                "id": 10000027, 
                "price": 100
            }, 
            {
                "id": 10000028, 
                "price": 100
            }, 
            {
                "id": 10000029, 
                "price": 100
            }
        ]
    }
    }'''
    urlinfo='https://api.weixin.qq.com/merchant/create?access_token='
    requ=postrequest(request,postinfo,urlinfo)
    return HttpResponse(requ)

def queryproduct(request):
    urlinfo='https://api.weixin.qq.com/merchant/get?access_token='
    postinfo='''{
    "product_id": "pDF3iYwktviE3BzU3BKiSWWi9Nkw"
    }'''
    postrequest(request,postinfo,urlinfo)
    return HttpResponse('SUCCESS')

def queryproductstatus(request):
    urlinfo='https://api.weixin.qq.com/merchant/getbystatus?access_token='
    postinfo='''{
    "status": 0
    }'''
    requ=postrequest(request,postinfo,urlinfo)
    return HttpResponse(requ)

def userregistershow(request):
    return render_to_response('registeruser.html')
    
    
#用户注册
@csrf_exempt
def userregister(request):
    IDcard = request.POST.get( 'IDcard', None )
    username = request.POST.get( 'username', None )
    email = request.POST.get( 'email', None)
    phonenum = request.POST.get( 'phonenumber', None)
    yourpw = request.POST.get( 'yourpw', None)
    xingming = request.POST.get( 'xingming', None)
    userhave=User.objects.filter(username=username)
    if len(userhave)==0:      
        user1 = User.objects.create_user(username=username, 
                email=email, password=yourpw,first_name=xingming)
        user1.save()
        
        u = User.objects.get(username=username)
        u1 = UserProfile.objects.get(user_id=u.id)
        u1.phonenumber=phonenum
        u1.IDcard=IDcard
        u1.save()
    else:
        return render_to_response('registeruser.html',{'userhave':'用户名已经存在！'})
    
    return render_to_response('index2.html')


#用户登录界面
def loginview(request):
    '''if request.user.is_authenticated():
            return render_to_response('index2.html')'''
    return render_to_response('login.html')

#用户登录提交
@csrf_exempt
def loginAction(request):
    username = request.POST.get( 'username', None )
    yourpw = request.POST.get( 'yourpw', None)
    user = authenticate(username=username,password=yourpw)  
    if user is not None:
        if user.is_active:  
            login(request, user) 
            #return render(request,'405.html',{'res':request.META['HTTP_USER_AGENT']})   
            return render(request,'index2.html')
    else:
        return render_to_response('login.html',{'userlogin':'用户名或密码不对，登录失败！'})
    
#欢迎界面  
def welcome(request):
    return render_to_response('welcome.html')

#刮刮卡界面
def guaguaka(request):
    return render_to_response('guaguaka.html')
#服饰下一页
def xiayiye(request):
    number=request.session['num']
    number=number+0
    num1=number*20
    num=number*20+20
    city=request.session['city']
    productFushi=clothes.objects.filter(clcity=city).order_by("-id")[num1:num]
    request.session['num']=request.session['num']+1
    #items =chain(city, productFushi)
    return render_to_response('xiayiye.html',locals())

#服饰下一页search
def xiayiyesearch(request):
    number=request.session['num']
    number=number+0
    num1=number*20
    num=number*20+20
    city=request.session['city']
    productFushi=clothes.objects.filter(clcity=city,clname__contains=fushisearch).order_by("-id")[num1:num]
    request.session['num']=request.session['num']+1
    #items =chain(city, productFushi)
    return render_to_response('xiayiye.html',locals())

#公益界面
@csrf_exempt
def fushisearch(request):
    request.session['num'] = 1
    fushisearch = request.POST.get( 'fushisearch', None )
    city=request.session['city']
    cityshiji=''
    if city=='beijing':
        cityshiji='北京'
    elif city=='wuhan':
        cityshiji='武汉'
    productFushi=clothes.objects.filter(clcity=city,clname__contains=fushisearch).order_by("-id")[0:10]
    return render_to_response('fushisearch.html',locals())

#城市选择
def citycity(city):
    if city=='beijing':
        cityshiji='北京'
    elif city=='wuhan':
        cityshiji='武汉'
    elif city=='shanghai':
        cityshiji='上海'
    elif city=='chongqing':
        cityshiji='重庆'
    elif city=='chengdu':
        cityshiji='成都'
    elif city=='shenzhen':
        cityshiji='深圳'
    elif city=='nanjing':
        cityshiji='南京'
    elif city=='tianjin':
        cityshiji='天津'
    elif city=='hangzhou':
        cityshiji='杭州'
    elif city=='guangzhou':
        cityshiji='广州'
    elif city=='xian':
        cityshiji='西安'
    elif city=='wuhan':
        cityshiji='武汉'
    else:
        cityshiji='暂无'
    return cityshiji

#商品界面
def productfushi(request,city,offsize):
    request.session['num'] = 1
    if city=='':
        city=beijing
    if offsize=='1':
        productFushi=clothes.objects.filter(clcity=city).order_by("-id")[0:20]
    elif offsize=='2':
        productFushi=clothes.objects.filter(clshi=city).order_by("-id")[0:20]
    else:
        return render_to_response('404_9.html')
    #city=request.GET.get('city', 'beijing')
    request.session['city'] = city
    cityshiji=citycity(city)
    #items =chain(city, productFushi)
    return render_to_response('productfushi.html',locals())

#公益界面
def gongyi(request):
    return render_to_response('gongyi.html')

#隐藏测试
def yincang(request):
    return render_to_response('yincang.html')

#改变城市
def changecity(request):
    return render_to_response('changecity.html')
#日历签到
def qiandao(request):
    return render_to_response('qiandao.html')
