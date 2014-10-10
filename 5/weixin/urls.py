# -*- coding: utf8 -*-



from django.conf.urls import patterns, include, url
import plus86.views
import bew.views
import settings,os
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'weixin.views.home', name='home'),
    # url(r'^weixin/', include('weixin.foo.urls')),
    url(r'^weixin', 'plus86.views.handleRequest'),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^$', 'plus86.views.current_datetime'),
    url(r'^create/createmenu$', 'plus86.views.creatmenu'),
    url(r'^create/deletemenu$', 'plus86.views.deletemenu'),
    url(r'^membercard/', 'plus86.views.membercard'),
    url(r'^register', 'plus86.views.register'),
    url(r'^userregister/', 'plus86.views.userregistershow'),
    url(r'^userregisteraction/', 'plus86.views.userregister'),
    url(r'^userlogin/', 'plus86.views.loginview'),  #用户登录界面
    url(r'^userloginaction/', 'plus86.views.loginAction'),  #用户登录动作
    url(r'^welcome/', 'plus86.views.welcome'),  #欢迎界面
    url(r'^guaguaka/', 'plus86.views.guaguaka'),  #刮刮卡界面
    url(r'^productfushi/([a-z]*)/([1-2])/$', 'plus86.views.productfushi'),  #服饰界面
    url(r'^fushidetail/(\d+)/$', 'plus86.views.fushidetail'),  #服饰细节
    url(r'^gongyi/', 'plus86.views.gongyi'),  #公益界面
    url(r'^gongyidetail/(\d+)/$', 'plus86.views.gongyidetail'),  #公益细节
    url(r'^yincang/', 'plus86.views.yincang'),  #隐藏测试
    url(r'^changecity/$', 'plus86.views.changecity'),  #改变城市
    url(r'^xiayiye/', 'plus86.views.xiayiye'),  #下一页
    url(r'^xiayiyesearch/', 'plus86.views.xiayiyesearch'),  #下一页search
    url(r'^fushisearch/', 'plus86.views.fushisearch'),  #服饰搜索
    url(r'^qiandao/$', 'plus86.views.qiandao'),  #日历签到
    url(r'^riqiqiandao/$', 'plus86.views.riqiqiandaoa'),  #日历签到xin
    url(r'^riqiqiandaoaction/$', 'plus86.views.riqiqiandaoaction'),  #日历签到xin
    url(r'^gonggao/$', 'plus86.views.gonggaoa'),  #公告
    url(r'^gonggaolishi/$', 'plus86.views.gonggaoalishi'),  #历史公告
    url(r'^gonggaodetail/(\d+)/$', 'plus86.views.gonggaodetail'),  #公告细节
    url(r'^huodong/$', 'plus86.views.huodongview'),  #活动
    url(r'^huodongsearch/$', 'plus86.views.huodongsearch'),  #活动search
    url(r'^huodongdetail/(\d+)/$', 'plus86.views.huodongdetail'),  #活动细节
    url(r'^zhifujiaoxue/$', 'plus86.views.zhifujiaoxue'),  #支付教学
    url(r'^zhaoshang/$', 'plus86.views.zhaoshang'),  #招商
    url(r'^qunfa/$', 'plus86.views.qunfa'),  #群发
    url(r'^qunfajiemian/$', 'plus86.views.qunfajiemian'),  #群发界面
    url(r'^uploadfile/$', 'plus86.views.uploadfile'),  #上传
    url(r'^useruploadfile/$', 'plus86.views.useruploadfile'),  #上传界面
    url(r'^checkmember/', 'plus86.views.checkmember'),
    url(r'^reg/', 'plus86.views.reg'),
    url(r'^checkweixininfo/', 'plus86.views.getweixininfo'),
    url(r'^createproduct/', 'plus86.views.createproduct'),
    url(r'^queryproductstatus/', 'plus86.views.queryproductstatus'),
    url(r'^plus86admin/', include(admin.site.urls)),
    
    #美食相关
    url(r'^productfoods/([a-z]*)/([1-2])/$', 'plus86.views.productfoods'),  #美食界面
    url(r'^foodsdetail/(\d+)/$', 'plus86.views.foodsdetail'),  #美食细节
    url(r'^foodschangecity/$', 'plus86.views.foodschangecity'),  #改变城市美食
    url(r'^foodsxiayiye/', 'plus86.views.foodsxiayiye'),  #下一页美食
    url(r'^foodsxiayiyesearch/', 'plus86.views.foodsxiayiyesearch'),  #下一页search美食
    url(r'^foodssearch/', 'plus86.views.foodssearch'),  #美食搜索
    #url(r'^site_media/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.STATIC_ROOT}),
    

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
#handler404 = 'plus86.views.page_not_found'
#handler500 = 'plus86.views.page_error'
