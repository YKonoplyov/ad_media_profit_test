from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/", include("spend.urls", namespace="spend")),
    path("api/v1/", include("revenue.urls", namespace="revenue")),
    path("__debug__/", include("debug_toolbar.urls")),
]
