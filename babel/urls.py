"""
babel URL Configuration

"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from catalog.views import home, newsroom, about, publication

urlpatterns = (
    [
        path("admin/", admin.site.urls),
        path("newsroom/", newsroom, name="newsroom"),
        path("about/", about, name="about"),
        path("publication/", publication, name="publication"),
        path("", home, name="home"),
    ]
    + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
)
