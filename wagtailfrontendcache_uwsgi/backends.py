from urllib.parse import urlparse

from django.core.exceptions import ImproperlyConfigured
from wagtail.contrib.frontend_cache.backends import BaseBackend

from .compat import uwsgi


class UWSGIBackend(BaseBackend):
    def __init__(self, params):
        self.cache_name = params.pop("CACHE_NAME", None)

        if self.cache_name is None:
            raise ImproperlyConfigured(
                "Missing CACHE_NAME value for backend. "
                "Check your uWSGI to get the proper cache name."
            )

    def purge(self, url):
        url_parsed = urlparse(url)
        uwsgi.cache_del(
            f"{url_parsed.netloc}{url_parsed.path}", self.cache_name
        )
