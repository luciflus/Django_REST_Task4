from rest_framework import serializers
from .models import Goods, Category, Company

class CategorySerializer(serializers.Serializer):
    category_name = serializers.CharField(max_length=20)
    def create(self, validated_data):
        return Category.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.category_name = validated_data['category_name']
        instance.save()
        return instance

class CompanySerializer(serializers.Serializer):
    name = serializers.CharField(max_length=20)
    address = serializers.CharField(max_length=50)
    def create(self, validated_data):
        return Company.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data['name']
        instance.address = validated_data['address']
        instance.save()
        return instance

class GoodsSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=30)
    price = serializers.IntegerField()
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all(), many=False)
    company = serializers.PrimaryKeyRelatedField(queryset=Company.objects.all(), many=False)
    def create(self, validated_data):
        return Goods.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data['name']
        instance.price = validated_data['price']
        instance.category = validated_data['category']
        instance.company = validated_data['company']
        instance.save()
        return instance