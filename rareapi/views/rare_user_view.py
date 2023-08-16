from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from rareapi.models import RareUser


class RareUserView(ViewSet):

    def retrieve(self, request, pk):
        rare_user = RareUser.objects.get(pk=pk)
        serializer = RareUserSerializer(rare_user)
        return Response(serializer.data)

    def list(self, request):
        RareUsers = RareUser.objects.all()
        serializer = RareUserSerializer(RareUsers, many=True)
        return Response(serializer.data)

class RareUserSerializer(serializers.ModelSerializer):
  
    class Meta:
        model = RareUser
        fields = ('id', 'user', 'bio', 'profile_image_url', 'created_on', 'active')