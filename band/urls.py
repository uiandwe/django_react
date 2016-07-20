__author__ = 'uiandwe'

from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
                       url(r'^$', 'band.views.all_bands'),
                       url(r'(?P<band_id>\d+)/$', 'band.views.band'),
                       )

