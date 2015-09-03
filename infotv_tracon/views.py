from django.contrib.admin.views.decorators import staff_member_required
from django.core.urlresolvers import reverse
from django.conf import settings
from django.shortcuts import redirect


@staff_member_required(login_url=settings.LOGIN_URL)
def infotv_edit_redirect_view(self, event):
    return redirect(reverse('infotv_view', args=(event,)) + '?edit=1')
