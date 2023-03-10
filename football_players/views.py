from rest_framework import generics  # в ветке generics много классов для представления django rest framework
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser, IsAuthenticated

from .models import FootballPlayers
from .permissions import IsAdminOrReadOnly
from .serializers import FootballPlayersSerializer


class FootballPlayersAPIListPagination(PageNumberPagination):  # класс пагинации только для FootballPlayersAPIList
    page_size = 3
    page_size_query_param = 'page_size'  # дополнительный параметр для ручного изменения числа записей-пишется в url ...&page_size=4 и будет 4 записи, а не 3.
    max_page_size = 10000


class FootballPlayersAPIList(generics.ListCreateAPIView):
    queryset = FootballPlayers.objects.all()
    serializer_class = FootballPlayersSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    pagination_class = FootballPlayersAPIListPagination


class FootballPlayersAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = FootballPlayers.objects.all()
    serializer_class = FootballPlayersSerializer
    permission_classes = (IsAuthenticated,)  # просматривать могут только авторизованные пользователи
    # authentication_classes = (TokenAuthentication, )  # аутентификация по токенам только для этого view


class FootballPlayerAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = FootballPlayers.objects.all()
    serializer_class = FootballPlayersSerializer
    permission_classes = (IsAdminOrReadOnly,)

