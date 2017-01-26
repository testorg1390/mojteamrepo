# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.utils.encoding import smart_text
import os
from .views import index,about_me

# admin.site.index_template = 'admin_index.html'
# admin.site.index_template = 'admin_index.html'

admin.site.site_header = smart_text('صفحه مدیریت وبسایت')
admin.site.site_title = smart_text('مدیریت وبسایت')
var_static = os.path.dirname(__file__)

urlpatterns = patterns('',
    # Examples:
    # (r'^media(?P<path>.*)$','django.views.static.serve',{'document_root':os.path.join(var_static,'media')}),
    # (r'^static(?P<path>.*)$','django.views.static.serve',{'document_root':os.path.join(var_static,'static')}),
    (r'^ckeditor/', include('ckeditor_uploader.urls')),
    url(r'^$',index.as_view(), name='index'),
    url(r'^about_me/$',about_me.as_view(), name='about_me'),
    url(r'contact_me/',include('contact_me.urls')),
    # url(r'^blog/', include('blog.urls')),
    url(r'post/', include('site_posts.urls')),
    url(r'account/', include('account.urls')),
    url(r'profile/', include('account_profile.urls')),
    url(r'khabarnameh/', include('khabarnameh.urls')),
    url(r'category/', include('site_category.urls')),
    url(r'menue/', include('menue.urls')),
    url(r'sabad/', include('sabad.urls')),
    url(r'download/', include('temperate_links.urls')),

    url(r'^captcha/', include('captcha.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
