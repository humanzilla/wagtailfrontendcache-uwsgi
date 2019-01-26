from django.conf.urls import url
from django.contrib import admin

from . import views

appname = 'wagtailfrontendcache_uwsgi'

urlpatterns = [
    url(
        r"^$",
        admin.site.admin_view(views.DashboardView.as_view()),
        name="wagtail_cache_setup",
    ),
    url(
        r"^flush/$",
        admin.site.admin_view(views.FlushCacheView.as_view()),
        name="wagtail_cache_setup",
    )
]
