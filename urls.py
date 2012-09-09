# -*- coding: utf-8 -*-
"""
Url's map "racine"
"""
from django.conf.urls.defaults import *
from django.conf import settings

from django.contrib import admin
admin.autodiscover()

import autobreadcrumbs
autobreadcrumbs.autodiscover()

from views import HomepageView, BatcaveIndex

from accounts.views import MyAccountView
from alliance.views import MyStructureCreateView, MyToolCreateView, DemandCreateView

#from sveedocuments.views.page import HelpPageView, PageIndexView, PageDetailsView, PageSourceView

urlpatterns = patterns('',
    url(r'^$', HomepageView.as_view(), name='homepage'),
    
    (r'^admin/', include(admin.site.urls)),
    
    (r'^accounts/', include('sveeaccounts.urls')),
    
    url(r'^batcave/$', BatcaveIndex.as_view(), name='batcave-index'),
    #(r'^batcave/documents/', include('sveedocuments.urls_board')),
    
    url(r'^demand/$', DemandCreateView.as_view(), name='demand-public-add'),
    
    url(r'^my/$', MyAccountView.as_view(), name='accounts-my'),
    url(r'^my/add/structure/$', MyStructureCreateView.as_view(success_list_url="accounts-my"), name='accounts-my-structure-add'),
    url(r'^my/suggest/tool/$', MyToolCreateView.as_view(success_list_url="accounts-my"), name='accounts-my-tool-add'),
    
    #url(r'^documents-help/$', HelpPageView.as_view(), name='documents-help'),
    #url(r'^sitemap/$', PageIndexView.as_view(), name='documents-index'),
    #url(r'^(?P<slug>[-\w]+)/$', PageDetailsView.as_view(), name='documents-page-details'),
    #url(r'^(?P<slug>[-\w]+)/source/$', PageSourceView.as_view(), name='documents-page-source'),
)
        
# En production (avec le debug_mode à False) ceci ne sera pas chargé
if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^medias/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
    )
