from django.conf import settings
from django.conf.urls import include
from django.views.decorators.csrf import csrf_exempt
from django.views.generic.base import RedirectView

from django.contrib import admin
from django.contrib.auth.views import LogoutView

admin.autodiscover()

from infotv.views import InfoTvView

from .views import infotv_edit_redirect_view, status_view
from django.urls import path, re_path


urlpatterns = [
    path('', include("kompassi_oauth2.urls")),
    path('', RedirectView.as_view(
            url="/events/{event_slug}/infotv/?slow=1".format(
                event_slug=settings.INFOTV_DEFAULT_EVENT
            )
        ),
    ),
    re_path(
        r"^edit/?$",
        infotv_edit_redirect_view,
        dict(event=settings.INFOTV_DEFAULT_EVENT),
    ),
    re_path(
        r"^events/(?P<event>[a-z0-9-]+)/infotv/?$",
        csrf_exempt(InfoTvView.as_view()),
        name="infotv_view",
    ),
    re_path(
        r"^events/(?P<event>[a-z0-9-]+)/infotv/edit/?$",
        infotv_edit_redirect_view,
        name="infotv_edit_redirect_view",
    ),
    path('admin/', admin.site.urls),
    re_path(r"^healthz/?$", status_view, name="status_view"),
    re_path(r"^logout/?$", LogoutView.as_view(), name="logout_view"),
]
