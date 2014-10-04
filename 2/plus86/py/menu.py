# -*- coding: utf-8 -*-
import sae
import web
import xml.etree.ElementTree as ET
import sae.const
import MySQLdb
import urllib2
import json
 
 
#自定义菜单    

 
def creatmenu():
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
          "name":"开始",
          "key":"begin"
      },
      {
           "type":"click",
           "name":"结束",
           "key":"end"
      },
      {
          "type":"click",
           "name":"游戏",
           "key":"play"   
       }]
 }'''
    url = 'https://api.weixin.qq.com/cgi-bin/menu/create?access_token='+token
    req = urllib2.Request(url, post)
    response = urllib2.urlopen(req)
    return response
 
#删除菜单    

def deletemenu():
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
 
