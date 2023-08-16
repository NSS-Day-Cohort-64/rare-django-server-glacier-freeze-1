from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from rareapi.models import GameType


class TagView(ViewSet):
    """Level up game types view"""

    def retrieve(self, request, pk):
        tag = GameType.objects.get(pk=pk)
        serializer = GameTypeSerializer(game_type)
        return Response(serializer.data)

    def list(self, request):
        game_types = GameType.objects.all()
        serializer = GameTypeSerializer(game_types, many=True)
        return Response(serializer.data)