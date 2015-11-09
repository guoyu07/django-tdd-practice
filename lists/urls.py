from django.conf.urls import patterns, include, url

from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^(\d+)/$', 'lists.views.view_list', name='view_list'),
                       url(r'^(\d+)/add_item$', 'lists.views.add_item', name='add_item'),
                       url('^new$', 'lists.views.new_list', name='new_list'),  # 操作数据库不需要加/
                       )