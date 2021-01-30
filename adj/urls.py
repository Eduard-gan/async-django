
from django.contrib import admin
from django.urls import path

from adj.views import index, async_index


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", index),
    path("async", async_index),
]
