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
    url(r'^$', 'bew.views.current_datetime'),
    url(r'^create/createmenu', 'plus86.views.creatmenu'),
    url(r'^create/deletemenu', 'plus86.views.deletemenu'),
    url(r'^membercard/', 'plus86.views.membercard'),
    url(r'^register', 'plus86.views.register'),
    url(r'^userregister/', 'plus86.views.userregistershow'),
    url(r'^userregisteraction/', 'plus86.views.userregister'),
    url(r'^userlogin/', 'plus86.views.loginview'),  #用户登录界面
    url(r'^userloginaction/', 'plus86.views.loginAction'),  #用户登录动作
    url(r'^checkmember/', 'plus86.views.checkmember'),
    url(r'^reg/', 'plus86.views.reg'),
    url(r'^checkweixininfo/', 'plus86.views.getweixininfo'),
    url(r'^createproduct/', 'plus86.views.createproduct'),
    url(r'^queryproductstatus/', 'plus86.views.queryproductstatus'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^site_media/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.STATIC_ROOT}),
    

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
