from django.conf import settings
from django.conf.urls import include, url
from django.views.decorators.csrf import csrf_exempt
from django.views.generic.base import RedirectView

from django.contrib import admin
from django.contrib.auth.views import LogoutView

admin.autodiscover()

from infotv.views import InfoTvView

from .views import infotv_edit_redirect_view, status_view


urlpatterns = [
    url(r"", include("kompassi_oauth2.urls")),
    url(
        r"^$",
        RedirectView.as_view(
            url="/events/{event_slug}/infotv/?slow=1".format(
                event_slug=settings.INFOTV_DEFAULT_EVENT
            )
        ),
    ),
    url(
        r"^edit/?$",
        infotv_edit_redirect_view,
        dict(event=settings.INFOTV_DEFAULT_EVENT),
    ),
    url(
        r"^events/(?P<event>[a-z0-9-]+)/infotv/?$",
        csrf_exempt(InfoTvView.as_view()),
        name="infotv_view",
    ),
    url(
        r"^events/(?P<event>[a-z0-9-]+)/infotv/edit/?$",
        infotv_edit_redirect_view,
        name="infotv_edit_redirect_view",
    ),
    url(r"^admin/", admin.site.urls),
    url(r"^healthz/?$", status_view, name="status_view"),
    url(r"^logout/?$", LogoutView.as_view(), name="logout_view"),
]
