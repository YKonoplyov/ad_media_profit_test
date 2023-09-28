from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, Serializer

from spend.models import SpendStatistic


class SpendStatisticModelSerializer(ModelSerializer):
    class Meta:
        model = SpendStatistic
        fields = "__all__"
