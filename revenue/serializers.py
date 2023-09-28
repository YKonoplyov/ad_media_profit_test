from rest_framework.serializers import ModelSerializer

from revenue.models import RevenueStatistic


class RevenueStatisticModelSerializer(ModelSerializer):
    class Meta:
        model = RevenueStatistic
        fields = "__all__"
