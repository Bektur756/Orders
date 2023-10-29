from rest_framework import serializers
from .models import OrderHistory
from django.db.models import Sum


class FileUploadSerializer(serializers.Serializer):
    file = serializers.FileField()


class OrderHistoryListSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='customer')
    spent_money = serializers.SerializerMethodField()
    gems = serializers.SerializerMethodField()

    class Meta:
        model = OrderHistory
        fields = ('username', 'spent_money', 'gems')

    def get_spent_money(self, obj):
        return OrderHistory.objects.filter(customer=obj.customer).aggregate(Sum('total'))['total__sum']

    def get_gems(self, obj):
        products = OrderHistory.objects.filter(customer=obj.customer).values_list('item', flat=True).distinct()
        return list(products)


class OrderHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderHistory
        fields = ('customer', 'item', 'total', 'quantity', 'date')
