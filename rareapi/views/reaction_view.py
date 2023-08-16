from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from rareapi.models import Reaction


class ReactionView(ViewSet):

    def retrieve(self, request, pk):
        reaction = Reaction.objects.get(pk=pk)
        serializer = ReactionSerializer(reaction)
        return Response(serializer.data)

    def list(self, request):
        reactions = Reaction.objects.all()
        serializer = ReactionSerializer(reactions, many=True)
        return Response(serializer.data)

class ReactionSerializer(serializers.ModelSerializer):
  
    class Meta:
        model = Reaction
        fields = ('id', 'label', 'image_url')