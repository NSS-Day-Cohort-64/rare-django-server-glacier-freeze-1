from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from rareapi.models import RareUser
from django.contrib.auth.models import User


class RareUserView(ViewSet):

    def retrieve(self, request, pk):
        rare_user = RareUser.objects.get(pk=pk)
        serializer = RareUserSerializer(rare_user)
        return Response(serializer.data)

    def list(self, request):
        RareUsers = RareUser.objects.all()
        serializer = RareUserSerializer(RareUsers, many=True)
        return Response(serializer.data)
    
    def update(self, request, pk):
        """handles PUT requests for updating a Comment"""
        rareuser = RareUser.objects.get(pk=pk)
        rareuser.bio =  request.data["bio"]
        rareuser.profile_image_url =  request.data["profile_image_url"]
        rareuser.user = User.objects.get(pk=request.data["user"])
        rareuser.created_on = request.data["created_on"]
        rareuser.active = request.data["active"]

        rareuser.save()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
    
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'password', 'last_login', 'is_superuser', 'username',
                  'first_name', 'last_name', 'email', 'is_staff', 'is_active',
                  'date_joined')

class RareUserSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False)
    class Meta:
        model = RareUser
        fields = ('id', 'user', 'bio', 'profile_image_url', 'created_on', 'active', 'full_name')
