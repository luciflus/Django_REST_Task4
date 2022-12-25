"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from goods import views

router = routers.DefaultRouter()
router.register('goods', views.GoodsViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/goods/', include(router.urls)),
    path('api/company/', views.CompanyCreateListView.as_view()),
    path('api/company/<int:pk>/', views.CompanyRetrieveUpdateDestroyAPIView.as_view()),
    path('api/category/', views.create_category),
]
