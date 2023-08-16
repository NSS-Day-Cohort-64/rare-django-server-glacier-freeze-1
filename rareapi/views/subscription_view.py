from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from rareapi.models import Subscription


class SubscriptionView(ViewSet):

    def retrieve(self, request, pk):
        subscription = Subscription.objects.get(pk=pk)
        serializer = SubscriptionSerializer(subscription)
        return Response(serializer.data)

    def list(self, request):
        subscriptions = Subscription.objects.all()
        serializer = SubscriptionSerializer(subscriptions, many=True)
        return Response(serializer.data)

class SubscriptionSerializer(serializers.ModelSerializer):
  
    class Meta:
        model = Subscription
        fields = ('id', 'follower', 'author', 'created_on', 'ended_on')