from django.conf.urls import url, include
from django.urls import reverse_lazy
from wagtail.admin.menu import MenuItem
from wagtail.core import hooks

from . import urls as wagtailfrontendcache_uwsgi_urls


class SetupMenuItem(MenuItem):
    def is_shown(self, request):
        return request.user.is_staff


@hooks.register("register_settings_menu_item")
def register_uwsgi_menu_item():
    return SetupMenuItem(
        "Frontend Cache",
        reverse_lazy("wagtailfrontendcache_uwsgi:setup"),
        classnames="icon icon-cogs",
        order=800,
    )


@hooks.register("register_admin_urls")
def register_admin_urls():
    return [
        url(
            r"^wagtailfrontendcache_uwsgi/",
            include(wagtailfrontendcache_uwsgi_urls, namespace='wagtailfrontendcache_uwsgi'),
        )
    ]
