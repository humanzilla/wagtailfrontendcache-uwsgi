from pathlib import Path
from setuptools import setup, find_packages

setup(
    version="1.0",
    name="wagtail-uwsgi-frontendcache",
    url="https://github.com/humanzilla/wagtailfrontendcache-uwsgi",
    author="Humanzilla",
    author_email="hello@humanzilla.com",
    description="Wagtail Frontend cache integration based in the uwsgi cache2 module.",
    long_description=(Path(__file__).parent / 'README.md').read_text(),
    long_description_content_type='text/markdown',

    packages=find_packages("."),
    include_package_data=True,
    zip_safe=False,
    python_requires=">=3.5.*",
    classifiers=[
        "Environment :: Web Environment",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3 :: Only",
        "Framework :: Django",
        "Framework :: Django :: 2.0",
        "Framework :: Wagtail",
        "Framework :: Wagtail :: 2",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Internet :: WWW/HTTP :: Site Management",
    ],
)
