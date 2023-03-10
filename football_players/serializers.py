from rest_framework import serializers

from .models import FootballPlayers


class FootballPlayersSerializer(serializers.ModelSerializer):
    class Meta:
        model = FootballPlayers
        fields = ("title", "content", "club")  # для указания всех полей нужно указывать "__all__
