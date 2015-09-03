from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.conf import settings
from django.shortcuts import redirect


@login_required
def infotv_edit_redirect_view(self, event):
    return redirect(reverse('infotv_view', args=(event,)) + '?edit=1')
