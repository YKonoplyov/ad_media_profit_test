from django.urls import path, include

from spend.views import SpendStatisticViewSet, GetSpendStatistic
from rest_framework.routers import DefaultRouter

spend_router = DefaultRouter()

spend_router.register("spend", SpendStatisticViewSet, basename="spend")

urlpatterns = [
    path('statistic/', GetSpendStatistic.as_view(), name="revenue-statistic"),
    path("spend/", include(spend_router.urls)),
]

app_name = "spend"
