from django.urls import path, include

from revenue.views import RevenueStatisticViewSet, GetRevenueStatistic
from rest_framework.routers import DefaultRouter

revenue_router = DefaultRouter()

revenue_router.register("revenue", RevenueStatisticViewSet, basename="revenue")

urlpatterns = [
    path("revenue/", include(revenue_router.urls)),
    path(
        "revenue_statistic/",
        GetRevenueStatistic.as_view(),
        name="revenue-statistic"
    )
]

app_name = "revenue"
