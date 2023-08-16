from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from rareapi.models import DemotionQueue, RareUser


class DemotionQueueView(ViewSet):

    def retrieve(self, request, pk):
        demotion_queue = DemotionQueue.objects.get(pk=pk)
        serializer = DemotionQueueSerializer(demotion_queue)
        return Response(serializer.data)

    def list(self, request):
        demotion_queues = DemotionQueue.objects.all()
        serializer = DemotionQueueSerializer(demotion_queues, many=True)
        return Response(serializer.data)

class DemotionRareUserSerializer(serializers.ModelSerializer):
    """JSON serializer for admin and approver_one"""
    class Meta:
        model = RareUser
        fields = ('id', 'user', 'bio', 'profile_image_url', 'active', 'full_name')


class DemotionQueueSerializer(serializers.ModelSerializer):
    admin = DemotionRareUserSerializer(many=False)
    approver_one = DemotionRareUserSerializer(many=False)
    class Meta:
        model = DemotionQueue
        fields = ('id', 'action', 'admin', 'approver_one')

        