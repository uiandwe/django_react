#-*- coding:utf-8 -*-
__author__ = 'uiandwe'

from django.conf.urls import patterns, include, url
from rest_framework.urlpatterns import format_suffix_patterns
from band.views import BandDetail
urlpatterns = patterns('',
                       url(r'^$', 'band.views.all_bands'),
                       url(r'^(?P<band_id>\d+)/$', 'band.views.band'),
                       url(r'^api/(?P<pk>[0-9]+)/$', BandDetail.as_view()),
                       )

urlpatterns = format_suffix_patterns(urlpatterns)