"""
URL Configuration
"""
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('data_fetcher/', include('data_fetcher.urls')),
    path('admin/', admin.site.urls),
]
