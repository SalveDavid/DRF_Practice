from .models import Customer, Order
from rest_framework import serializers


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'


class CustomerSerializer(serializers.ModelSerializer):
    orders = OrderSerializer(read_only=True, many=True)

    class Meta:
        model = Customer
        fields = '__all__'
