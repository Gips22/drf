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
from django.urls import path, include, re_path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

from football_players.views import *
from rest_framework import routers



urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/drf-auth/', include('rest_framework.urls')),  # Аутентификация по session id (session-based authentication)
    path('api/v1/football/', FootballPlayersAPIList.as_view()),
    path('api/v1/football/<int:pk>/', FootballPlayersAPIUpdate.as_view()),
    path('api/v1/footballdelete/<int:pk>/', FootballPlayerAPIDestroy.as_view()),
    path('api/v1/auth/', include('djoser.urls')),  # djoser
    re_path(r'^auth/', include('djoser.urls.authtoken')),  # djoser. Строчка отвечает за авторизацию по токенам
    path('api/v1/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/v1/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/v1/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]

# urls для route и без permissions

# router = routers.DefaultRouter()  # создаем роутер для того чтобы не писать несколько path, а только одну
# router.register(r'football_players', FootballPlayersViewSet)


# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('api/v1/', include(router.urls)),  # https://127.0.0.1:8000/api/v1/football_players/ тут это заменяет 2 роута: где мы смотрм список статей и где можем менять или удалять
#
# ]
