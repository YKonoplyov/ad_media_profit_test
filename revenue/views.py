from rest_framework.viewsets import ModelViewSet

from revenue.models import RevenueStatistic
from revenue.serializers import RevenueStatisticSerializer


class RevenueStatisticViewSet(ModelViewSet):
    serializer_class = RevenueStatisticSerializer
    queryset = RevenueStatistic.objects.all()
