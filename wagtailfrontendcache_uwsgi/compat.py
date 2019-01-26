from typing import Optional


class UwsgiModule:
    numproc: int # The number of processes/workers currently running.
    started_on: int # The Unix timestamp of uWSGI’s startup.
    opt: dict # The current configuration options, including any custom placeholders.
    magic_table: dict # The magic table of configuration placeholders.

    def get_option(self, name: str): ...

    def set_option(self, name: str, value: str): ...

    def cache_get(self, key: str, cache: Optional[str]): ...

    def cache_set(self, key, value: bytes, expires: Optional[int], cache: Optional[str]): ...

    def cache_update(self, key, value: bytes, expires: Optional[int], cache: Optional[str]): ...

    def cache_exists(self, key: str, cache: Optional[str]): ...

    def cache_del(self, key: str, cache: Optional[str]): ...

    def cache_clear(self, cache: Optional[str]): ...


try:
    import uwsgi
except ImportError:
    uwsgi = UwsgiModule()
