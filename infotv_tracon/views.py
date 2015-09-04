from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.conf import settings
from django.shortcuts import redirect


import infotv.views


# Monkey patch infotv bootstrap template to add viewport tag
infotv.views.TEMPLATE = u"""
<!doctype html>
<html lang="en">
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta charset="UTF-8">
    <script>
    if(typeof webView !== "undefined") {
      webView.getSettings().setLayoutAlgorithm(WebSettings.LayoutAlgorithm.NORMAL);
    }
    </script>
</head>
<body>
    <div id="tv"></div>
    <script>var Options = %(options_json)s;</script>
    <script src="%(bundle_path)s"></script>
</body>
</html>
"""


@login_required
def infotv_edit_redirect_view(self, event):
    return redirect(reverse('infotv_view', args=(event,)) + '?edit=1')
