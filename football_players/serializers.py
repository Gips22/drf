import io

from rest_framework import serializers
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer

from .models import FootballPlayers


class FootballPlayersSerializer(serializers.HiddenField):
    class Meta:
        model = FootballPlayers
        fields = ("title", "content", "club")  # для указания всех полей нужно указывать "__all__

# def encode():
#     model = FootballPlayersModel('...')
#     model_sr = FootballPlayersSerializer(model)
#     print(model_sr.data, type(model_sr.data), sep='\n')
#     json = JSONRenderer().render(model_sr.data)
#     print(json)
#
#
# def decode():
#     stream = io.BytesIO(b'{"title":"Cristiano R","content":"Content: ..."}')
#     data = JSONParser().parse(stream)
#     serializer = FootballPlayersSerializer(data=data)
#     serializer.is_valid()
#     print(serializer.validated_data)
