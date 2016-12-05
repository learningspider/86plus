#!/usr/bin/env python
#-*- coding: utf-8 -*-
import urllib,urllib2
class yumi:
    def __init__(self):
        self.token = ''
        self.name = 'spider1983'
        self.pwd = '1'
        self.pid = ''

    def loginIn(self):
        postData = {"uid":self.name,"pwd":self.pwd}
        requrl = 'http://api.jyzszp.com/Api/index/loginIn'
        params = urllib.urlencode(postData);
        req = urllib2.Request(url=requrl, data=params)
        res_data = urllib2.urlopen(req)
        res = res_data.read()
        self.token = res.split('|')[2]



    def getMobilenum(self):
        postData = {'pid':self.pid,"uid": self.name, "token": self.token}


if __name__ == '__main__':
    while True:
        pass