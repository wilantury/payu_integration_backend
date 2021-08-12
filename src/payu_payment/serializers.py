
from rest_framework import serializers
from .models import LogPurchase


class LogPurchaseSerializer(serializers.ModelSerializer):

    class Meta:
        model = LogPurchase
        fields = '__all__'