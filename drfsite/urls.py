from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from rest_framework import permissions

from football_players.views import *

schema_view = get_schema_view(
    openapi.Info(
        title="API documentation",
        default_version='v1',
        description="API documentation",
        terms_of_service="https://www.example.com/policies/terms/",
        contact=openapi.Contact(email="xxx@xxx.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

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
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
