from django.forms import model_to_dict
from rest_framework import generics, viewsets  # в ветке generics много классов для представления django rest framework
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser, IsAuthenticated
from rest_framework.authentication import TokenAuthentication

from .models import FootballPlayers, Club
from .permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly
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

######
# Общий класс для обработки всех роутов без использования permissions
# class FootballPlayersViewSet(viewsets.ModelViewSet):  # Этот класс основанный на ModelViewSet заменяет у нас все классы снизу (только еще роуты поменяем)
#     queryset = FootballPlayers.objects.all()
#     serializer_class = FootballPlayersSerializer
#
#     @action(methods=['get'], detail=True)  # это мы с помощью декоратора создаем дополнительный маршрут (по дефолту их только 2). detail=true это значит что возвращается одна запись, а если false- то список категорий будет возвращаться
#     def category(self, request, pk=None):  # новый маршрут формируется используя имя метода category
#         cats = Club.objects.get(pk=pk)
#         return Response({'cats': cats.name})

#######
# class FootballPlayersAPIList(generics.ListCreateAPIView):  # класс для упрощенной работы. Включает в себя как метод get так и put
#     queryset = FootballPlayers.objects.all()
#     serializer_class = FootballPlayersSerializer

# class FootballPlayersAPIUpdate(generics.UpdateAPIView):  # UpdateAPIView позволяет выполнять тут только 2 запроса: put и patch
#     queryset = FootballPlayers.objects.all()  # этот запрос ленивый поэтому тут не будет каждый раз делаться запрос в БД.
#     serializer_class = FootballPlayersSerializer
#
#
# class FootballPlayersAPIDetailView(generics.RetrieveUpdateDestroyAPIView):  # RetrieveUpdateDestroyAPIView позволяет сразу и читать и изменять и удалять данные
#     queryset = FootballPlayers.objects.all()
#     serializer_class = FootballPlayersSerializer
##########
# class FootballPlayersAPIView(APIView):   # класс APIView стоит во главе всех классов в иерархии DRF
#     def get(self, request):
#         w = FootballPlayers.objects.all()
#         return Response({'posts': FootballPlayersSerializer(w, many=True).data})
#
#     def post(self, request):
#         serializer = FootballPlayersSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#
#         return Response({'post': serializer.data})
#
#     def put(self, request, *args, **kwargs):
#         pk = kwargs.get("pk", None)
#         if not pk:
#             return Response({"error": "Method PUT not allowed"})
#
#         try:
#             instance = FootballPlayers.objects.get(pk=pk)
#         except:
#             return Response({"error": "Object does not exists"})
#
#         serializer = FootballPlayersSerializer(data=request.data, instance=instance)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response({"post": serializer.data})
#
#     def delete(self, request, *args, **kwargs):
#         pk = kwargs.get("pk", None)
#         if not pk:
#             return Response({"error": "Method DELETE not allowed"})
#
#         # здесь код для удаления записи с переданным pk
#
#         return Response({"post": "delete post " + str(pk)})

# class FootballPlayersAPIView(generics.ListAPIView):
#     queryset = FootballPlayers.objects.all()
#     serializer_class = FootballPlayersSerializer
