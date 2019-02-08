import json

from django import forms
from django.http import HttpResponse
from django.views.generic import TemplateView
from wagtail.contrib.frontend_cache.utils import get_backends

from .compat import uwsgi


class DashboardView(TemplateView):
    template_name = "wagtailfrontendcache_uwsgi/dashboard.html"

    def get_context_data(self, **kwargs):
        uwsgi_backend = get_backends().get('uwsgi', None)
        kwargs['cache_keys'] = uwsgi_backend.get_cache_keys() if uwsgi_backend else []
        return super().get_context_data(**kwargs)


class ConfirmForm(forms.Form):
    confirm = forms.BooleanField(
        error_messages={
            "required": "Please confirm you wan't to continue with the action"
        }
    )


def flush_cache(request):
    form = ConfirmForm(data=request.POST or None)

    if form.is_valid():
        uwsgi.cache_clear()
        return HttpResponse(data=json.dumps({"ok": True}), status=200)

    return HttpResponse(
        data=json.dumps({"ok": False, "errors": form.errors}), status=400
    )
