from django.urls import path, include

from spend.views import SpendStatisticViewSet, GetSpendStatistic
from rest_framework.routers import DefaultRouter

spend_router = DefaultRouter()

spend_router.register("spend", SpendStatisticViewSet)

urlpatterns = [
    path("", include(spend_router.urls)),
    path("spend_statistic/", GetSpendStatistic.as_view(), name="spend-statistic"),
]

app_name = "spend"
