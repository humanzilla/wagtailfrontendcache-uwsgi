from setuptools import setup, find_packages

setup(
    name='wagtail-uwsgi-frontendcache',
    version='1.0',
    packages=find_packages('.'),
    include_package_data=True,
    zip_safe=False,
    python_requires=">=3.5.*",
)
