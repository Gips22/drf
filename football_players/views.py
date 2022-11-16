from django.forms import model_to_dict
from rest_framework import generics, viewsets
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import action

from .models import FootballPlayers, Club
from .serializers import FootballPlayersSerializer


class FootballPlayersViewSet(viewsets.ModelViewSet):  # Этот класс основанный на ModelViewSet заменяет у нас все классы снизу (только еще роуты поменяем)
    queryset = FootballPlayers.objects.all()
    serializer_class = FootballPlayersSerializer

    @action(methods=['get'], detail=True)  # это мы с помощью декоратора создаем дополнительный маршрут (по дефолту их только 2)
    def category(self, request, pk=None):  # новый маршрут формируется используя имя метода category
        cats = Club.objects.get(pk=pk)
        return Response({'cats': cats.name})


# class FootballPlayersAPIList(generics.ListCreateAPIView):  # класс для упрощенной работы. Включает в себя как метод get так и put
#     queryset = FootballPlayers.objects.all()
#     serializer_class = FootballPlayersSerializer

# class FootballPlayersAPIUpdate(generics.UpdateAPIView):  # UpdateAPIView позволяет выполнять тут только 2 запроса: put и patch
#     queryset = FootballPlayers.objects.all()  # этот запрос ленивый поэтому тут не будет каждый раз делаться запрос в БД.
#     serializer_class = FootballPlayersSerializer
#
#
# class FootballPlayersAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = FootballPlayers.objects.all()
#     serializer_class = FootballPlayersSerializer
##########
# class FootballPlayersAPIView(APIView):
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
