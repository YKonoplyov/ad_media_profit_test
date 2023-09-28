from django.db.models import Sum
from django.db.models.functions import Coalesce

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from spend.models import SpendStatistic
from spend.serializers import SpendStatisticModelSerializer, SpendStatisticSerializer


class GetSpendStatistic(APIView):
    def get_serializer_class(self, request):
        if self.request.method == "GET":
            return SpendStatisticSerializer

    def get_queryset(self):
        queryset = SpendStatistic.objects.values("name", "date").annotate(
            spend_sum=Sum("spend"),
            impressions_sum=Sum("impressions"),
            clicks_sum=Sum("clicks"),
            conversion_sum=Sum("conversion"),
            revenue_sum=Sum("revenue"),
        ).annotate(
            revenue_sum=Coalesce("revenue_sum", 0),
        )
        return queryset

    def get(self, request):
        queryset_data = list(self.get_queryset())
        print(queryset_data)
        serializer_class = self.get_serializer_class(request)
        serializer = serializer_class(data=queryset_data, many=True)
        print(serializer)
        if serializer.is_valid():
            return Response(serializer.data)


class SpendStatisticViewSet(ModelViewSet):
    serializer_class = SpendStatisticModelSerializer
    queryset = SpendStatistic.objects.all()
