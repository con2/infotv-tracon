from django.conf import settings
from django.conf.urls import patterns, include, url
from django.views.decorators.csrf import csrf_exempt
from django.views.generic.base import RedirectView

from django.contrib import admin
admin.autodiscover()

from infotv.views import InfoTvView

urlpatterns = patterns('',
    url(r'', include('kompassi_oauth2.urls')),
    url(r'^$', RedirectView.as_view(url="/events/{event_slug}/infotv/".format(event_slug=settings.INFOTV_DEFAULT_EVENT_SLUG))),
    url(r'^events/(?P<event>[a-z0-9-]+)/infotv/?$', csrf_exempt(InfoTvView.as_view())),
    url(r'^admin/', include(admin.site.urls)),
)
