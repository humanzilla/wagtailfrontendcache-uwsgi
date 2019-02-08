from typing import Iterable
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

    def get_cache_keys(self) -> Iterable[str]:
        cache_keys = uwsgi.cache_keys(self.cache_name)
        if not cache_keys:
            return []
        return map(lambda key: key.decode(), uwsgi.cache_keys(self.cache_name))

    def purge(self, url):
        url_parsed = urlparse(url)
        uwsgi.cache_del(
            f"http://127.0.0.1:8000{url_parsed.path}", self.cache_name
        )
        uwsgi.cache_del(
            f"http://localhost:8000{url_parsed.path}", self.cache_name
        )
        uwsgi.cache_del(
            f"{url_parsed.netloc}{url_parsed.path}", self.cache_name
        )
