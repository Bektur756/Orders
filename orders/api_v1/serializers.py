from rest_framework import serializers
from .models import Product
from django.db.models import Sum


class FileUploadSerializer(serializers.Serializer):
    file = serializers.FileField()


class ProductListSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='customer')
    spent_money = serializers.SerializerMethodField()
    gems = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ('username', 'spent_money', 'gems')

    def get_spent_money(self, obj):
        return Product.objects.filter(customer=obj.customer).aggregate(Sum('total'))['total__sum']

    def get_gems(self, obj):
        products = Product.objects.filter(customer=obj.customer).values_list('item', flat=True).distinct()
        return list(products)


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('customer', 'item', 'total', 'quantity', 'date')
