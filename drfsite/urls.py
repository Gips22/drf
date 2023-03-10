from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

from football_players.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/drf-auth/', include('rest_framework.urls')), # Аутентификация по session id (session-based authentication)
    path('api/v1/football/', FootballPlayersAPIList.as_view()),
    path('api/v1/football/<int:pk>/', FootballPlayersAPIUpdate.as_view()),
    path('api/v1/footballdelete/<int:pk>/', FootballPlayerAPIDestroy.as_view()),
    path('api/v1/auth/', include('djoser.urls')),  # djoser
    re_path(r'^auth/', include('djoser.urls.authtoken')),  # djoser. Строчка отвечает за авторизацию по токенам
    path('api/v1/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/v1/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/v1/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]
