from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, Serializer

from spend.models import SpendStatistic


class SpendStatisticModelSerializer(ModelSerializer):
    class Meta:
        model = SpendStatistic
        fields = "__all__"


class SpendStatisticSerializer(Serializer):
    name = serializers.CharField(max_length=255)
    date = serializers.DateField()
    spend_sum = serializers.DecimalField(max_digits=100, decimal_places=2)
    impressions_sum = serializers.IntegerField()
    clicks_sum = serializers.IntegerField()
    conversion_sum = serializers.IntegerField()
    revenue_sum = serializers.DecimalField(max_digits=100, decimal_places=2)
