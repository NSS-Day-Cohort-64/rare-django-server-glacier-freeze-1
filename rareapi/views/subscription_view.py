from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from rareapi.models import Subscription, RareUser


class SubscriptionView(ViewSet):

    def retrieve(self, request, pk):
        subscription = Subscription.objects.get(pk=pk)
        serializer = SubscriptionSerializer(subscription)
        return Response(serializer.data)

    def list(self, request):
        subscriptions = Subscription.objects.all()
        serializer = SubscriptionSerializer(subscriptions, many=True)
        return Response(serializer.data)
    
    def update(self, request, pk):
        """handles PUT requests for updating a Comment"""
        subscription = Subscription.objects.get(pk=pk)
        subscription.follower = RareUser.objects.get(pk=request.data["follower"])
        subscription.author = RareUser.objects.get(pk=request.data["author"])
        subscription.created_on = request.data["created_on"]
        subscription.ended_on = request.data["ended_on"]

        subscription.save()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
    
    def create(self, request):
        """Handle POST operations """
        follower = RareUser.objects.get(pk=request.data["follower"])
        author = RareUser.objects.get(pk=request.data["author"])

        subscription = Subscription.objects.create(
            follower=follower,
            author=author
        )
        serializer = SubscriptionSerializer(subscription)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
class SubscriptionUserSerializer(serializers.ModelSerializer):
    """JSON serializer for author and follower of subscription"""
    class Meta:
        model = RareUser
        fields = ('id', 'user', 'bio', 'profile_image_url', 'active', 'full_name')

class SubscriptionSerializer(serializers.ModelSerializer):
    follower= SubscriptionUserSerializer(many=False)
    author= SubscriptionUserSerializer(many=False)
    class Meta:
        model = Subscription
        fields = ('id', 'follower', 'author', 'created_on', 'ended_on')