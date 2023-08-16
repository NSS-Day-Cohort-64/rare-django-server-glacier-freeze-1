from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from rareapi.models import PostTag, Tag, Post


class PostTagView(ViewSet):

    def retrieve(self, request, pk):
        post_tag = PostTag.objects.get(pk=pk)
        serializer = PostTagSerializer(post_tag)
        return Response(serializer.data)

    def list(self, request):
        post_tags = PostTag.objects.all()
        serializer = PostTagSerializer(post_tags, many=True)
        return Response(serializer.data)

    def create(self, request):
        """Handle POST operations """
        tag = Tag.objects.get(pk=request.data['tag'])
        post = Post.objects.get(pk=request.data['post'])

        post_tag = PostTag.objects.create(
            tag = tag,
            post = post 
        )
        serializer = PostTagSerializer(post_tag)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class PostTagPostSerializer(serializers.ModelSerializer):
    """JSON serializer for post associated with this post tag"""
    class Meta:
        model = Post
        fields = ('id', 'user', 'category', 'title', 'publication_date', 'image_url', 'content', 'approved')

class PostTagTagSerializer(serializers.ModelSerializer):
    """JSON serializer for post associated with this comment"""
    class Meta:
        model = Tag
        fields = ('id', 'label')

class PostTagSerializer(serializers.ModelSerializer):
    tag=PostTagTagSerializer(many=False)
    post= PostTagPostSerializer(many=False)
    class Meta:
        model = Post
        fields = ('id', 'tag', 'post')