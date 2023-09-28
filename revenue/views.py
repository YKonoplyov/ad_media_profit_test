from rest_framework.viewsets import ModelViewSet

from revenue.models import RevenueStatistic
from revenue.serializers import RevenueStatisticSerializer
from revenue.serializers import (
    RevenueStatisticModelSerializer,
)


class RevenueStatisticViewSet(ModelViewSet):
    serializer_class = RevenueStatisticModelSerializer
    queryset = RevenueStatistic.objects.all()
