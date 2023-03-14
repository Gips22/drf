from rest_framework import generics  # в ветке generics много классов для представления django rest framework
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser, IsAuthenticated
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from .models import FootballPlayers
from .permissions import IsAdminOrReadOnly
from .serializers import FootballPlayersSerializer


class FootballPlayersAPIListPagination(PageNumberPagination):  # класс пагинации только для FootballPlayersAPIList
    """Класс для пагинации списка футболистов."""
    page_size = 3
    page_size_query_param = 'page_size'  # дополнительный параметр для ручного изменения числа записей-пишется в url ...&page_size=4 и будет 4 записи, а не 3.
    max_page_size = 10000


class FootballPlayersAPIList(generics.ListCreateAPIView):
    """ Класс для отображения списка футболистов и создания новых футболистов."""
    queryset = FootballPlayers.objects.all()
    serializer_class = FootballPlayersSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    pagination_class = FootballPlayersAPIListPagination

    @swagger_auto_schema(
        operation_summary="Список футболистов",
        responses={
            200: openapi.Response("Список футболистов", FootballPlayersSerializer(many=True))
        },
        tags=["Football Players"]
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Добавление нового футболиста",
        request_body=FootballPlayersSerializer,
        responses={
            201: openapi.Response("Футболист создан", FootballPlayersSerializer)
        },
        tags=["Football Players"]
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class FootballPlayersAPIUpdate(generics.RetrieveUpdateAPIView):
    """Класс для обновления информации о футболисте."""
    queryset = FootballPlayers.objects.all()
    serializer_class = FootballPlayersSerializer
    permission_classes = (IsAuthenticated,)  # просматривать могут только авторизованные пользователи

    @swagger_auto_schema(
        operation_summary="Обновление информации о футболисте",
        request_body=FootballPlayersSerializer,
        responses={
            200: openapi.Response("Информация о футболисте обновлена", FootballPlayersSerializer)
        },
        tags=["Football Players"]
    )
    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)


class FootballPlayerAPIDestroy(generics.RetrieveDestroyAPIView):
    """Класс для удаления футболиста из списка."""
    queryset = FootballPlayers.objects.all()
    serializer_class = FootballPlayersSerializer
    permission_classes = (IsAdminOrReadOnly,)

    @swagger_auto_schema(
        operation_summary="Удаление футболиста",
        responses={
            204: "Футболист удален"
        },
        tags=["Football Players"]
    )
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)
