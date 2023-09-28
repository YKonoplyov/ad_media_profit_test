from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, Serializer

from revenue.models import RevenueStatistic


class RevenueStatisticModelSerializer(ModelSerializer):
    class Meta:
        model = RevenueStatistic
        fields = "__all__"


class RevenueStatisticSerializer(Serializer):
    name = serializers.CharField(max_length=255)
    date = serializers.DateField()
    revenue_sum = serializers.DecimalField(max_digits=100, decimal_places=2)
    spend_sum = serializers.DecimalField(max_digits=100, decimal_places=2)
    impressions_sum = serializers.IntegerField()
    clicks_sum = serializers.IntegerField()
    conversion_sum = serializers.IntegerField()
