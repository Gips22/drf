"""drfsite URL Configuration

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

from football_players.views import *
from rest_framework import routers

router = routers.SimpleRouter()  # создаем роутер для того чтобы не писать несколько path, а только одну
router.register(r'football_players', FootballPlayersViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),  # https://127.0.0.1:8000/api/v1/football_players/ тут это заменяет 2 роута: где мы смотрм список статей и где можем менять или удалять
    # path('api/v1/womenlist/', WomenAPIList.as_view()),
    # path('api/v1/womenlist/<int:pk>/', WomenAPIUpdate.as_view()),
    # path('api/v1/womendetail/<int:pk>/', WomenAPIDetailView.as_view()),
]
