from django.urls import path, include

from revenue.views import RevenueStatisticViewSet
from rest_framework.routers import DefaultRouter

revenue_router = DefaultRouter()

revenue_router.register("revenue", RevenueStatisticViewSet, basename="revenue")

urlpatterns = [
    path("revenue/", include(revenue_router.urls)),
]

app_name = "revenue"
