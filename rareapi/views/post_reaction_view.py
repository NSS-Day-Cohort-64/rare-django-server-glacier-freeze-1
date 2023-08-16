from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from rareapi.models import PostReaction, Post, RareUser


class PostReactionView(ViewSet):

    def retrieve(self, request, pk):
        post_reaction = PostReaction.objects.get(pk=pk)
        serializer = PostReactionSerializer(post_reaction)
        return Response(serializer.data)

    def list(self, request):
        post_reactions = PostReaction.objects.all()
        serializer = PostReactionSerializer(post_reactions, many=True)
        return Response(serializer.data)

class PostReactionUserSerializer(serializers.ModelSerializer):
    """JSON serializer for author of comment"""
    class Meta:
        model = RareUser
        fields = ('id', 'user', 'bio', 'profile_image_url', 'active', 'full_name')

class PostReactionPostSerializer(serializers.ModelSerializer):
    """JSON serializer for post associated with this comment"""
    class Meta:
        model = Post
        fields = ('id', 'user', 'category', 'title', 'publication_date', 'image_url', 'content', 'approved')

class PostReactionSerializer(serializers.ModelSerializer):
    user= PostReactionUserSerializer(many=False)
    post = PostReactionPostSerializer(many=False)
    class Meta:
        model = PostReaction
        fields = ('id', 'user', 'post', 'reaction')

