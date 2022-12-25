import json
from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics, viewsets
from django.http import JsonResponse
from rest_framework.parsers import JSONParser

from .models import Category, Company, Goods
from .serializers import CategorySerializer, CompanySerializer, GoodsSerializer

class GoodsViewSet(viewsets.ModelViewSet):
    queryset = Goods.objects.all()
    serializer_class = GoodsSerializer

class CompanyCreateListView(generics.ListCreateAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

class CompanyRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

@csrf_exempt
def create_category(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        new_category = CategorySerializer(data=data)
        if new_category.is_valid():
            new_category.save()
            return JsonResponse(new_category.data, status=201)
        return JsonResponse(new_category.errors, status=400)
    if request.method == 'GET':
        categoryes = Category.objects.all()
        category_serializer = CategorySerializer(categoryes, many=True)
        return JsonResponse(category_serializer.data, safe=False)