from django.db.models import Sum
from django.db.models.functions import Coalesce

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from spend.models import SpendStatistic
from spend.serializers import SpendStatisticModelSerializer, SpendStatisticSerializer


# Create your views here.

class SpendStatisticViewSet(ModelViewSet):
    serializer_class = SpendStatisticModelSerializer
    queryset = SpendStatistic.objects.all()
