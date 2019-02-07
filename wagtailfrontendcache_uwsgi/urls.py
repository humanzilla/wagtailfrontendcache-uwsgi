from django.conf.urls import url
from django.contrib import admin

from . import views

app_name = 'wagtailfrontendcache_uwsgi'

urlpatterns = [
    url(
        r"^$",
        admin.site.admin_view(views.DashboardView.as_view()),
        name="setup",
    ),
    url(
        r"^flush/$",
        admin.site.admin_view(views.flush_cache),
        name="flush",
    )
]
