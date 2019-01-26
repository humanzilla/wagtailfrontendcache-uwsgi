from django.conf.urls import url, include
from wagtail.core import hooks

from . import urls as wagtailfrontendcache_uwsgi_urls


@hooks.register("register_admin_urls")
def register_admin_urls():
    return [
        url(
            r"^wagtailfrontendcache_uwsgi/",
            include(wagtailfrontendcache_uwsgi_urls),
        )
    ]
