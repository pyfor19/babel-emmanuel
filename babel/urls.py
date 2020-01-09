"""
babel URL Configuration

"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from catalog.views import index

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", index, name="catalog_index"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
