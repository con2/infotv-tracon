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
    <script>
    // https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/assign#Polyfill
    if (typeof Object.assign != 'function') {
    Object.assign = function(target, varArgs) { // .length of function is 2
        'use strict';
        if (target == null) { // TypeError if undefined or null
        throw new TypeError('Cannot convert undefined or null to object');
        }

        var to = Object(target);

        for (var index = 1; index < arguments.length; index++) {
        var nextSource = arguments[index];

        if (nextSource != null) { // Skip over if undefined or null
            for (var nextKey in nextSource) {
            // Avoid bugs when hasOwnProperty is shadowed
            if (Object.prototype.hasOwnProperty.call(nextSource, nextKey)) {
                to[nextKey] = nextSource[nextKey];
            }
            }
        }
        }
        return to;
    };
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
