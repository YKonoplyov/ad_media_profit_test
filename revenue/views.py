from django.db.models import Sum
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from revenue.models import RevenueStatistic
from revenue.serializers import (
    RevenueStatisticModelSerializer,
    RevenueStatisticSerializer,
)


class RevenueStatisticViewSet(ModelViewSet):
    serializer_class = RevenueStatisticModelSerializer
    queryset = RevenueStatistic.objects.all()


class GetRevenueStatistic(APIView):
    def get_serializer_class(self, request):
        if self.request.method == "GET":
            return RevenueStatisticSerializer

    def get_queryset(self):
        queryset = RevenueStatistic.objects.values("name", "date").annotate(
            revenue_sum=Sum("revenue"),
            spend_sum=Sum("spend"),
            impressions_sum=Sum("spend__impressions"),
            clicks_sum=Sum("spend__clicks"),
            conversion_sum=Sum("spend__conversion"),
        )
        return queryset

    def get(self, request: Request):
        queryset_data = list(self.get_queryset())
        serializer_class = self.get_serializer_class(request)
        serializer = serializer_class(data=queryset_data, many=True)
        if serializer.is_valid():
            return Response(serializer.data)
