from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from infotv.views import InfoTvView

urlpatterns = patterns('',
    url(r'', include('kompassi_oauth2.urls')),
    url(r'^events/(?P<event>[a-z0-9-]+)/infotv/?$', csrf_exempt(InfoTvView.as_view())),
    url(r'^admin/', include(admin.site.urls)),
)
