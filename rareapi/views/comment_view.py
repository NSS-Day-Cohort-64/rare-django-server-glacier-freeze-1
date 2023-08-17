from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from rareapi.models import Comment, Post, RareUser

class CommentView(ViewSet):
    """Comment views"""

    def list(self, request):
        """handles GET requests to return a list of comments"""
        comments = Comment.objects.all()
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def retrieve(self, request, pk):
        comment = Comment.objects.get(pk=pk)
        serializer = CommentSerializer(comment)
        return Response(serializer.data)
    
    def update(self, request, pk):
        """handles PUT requests for updating a Comment"""
        comment = Comment.objects.get(pk=pk)
        post = Post.objects.get(pk=request.data['post'])
        comment.post= post
        comment.author = RareUser.objects.get(pk=request.data["author"])
        comment.content = request.data["content"]

        comment.save()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
    
    def create(self, request):
        """Handle POST operations 
        created_on field will automatically be filled in with current date"""
        post = Post.objects.get(pk=request.data['post'])
        author = RareUser.objects.get(pk=request.data["author"])

        comment = Comment.objects.create(
            post=post,
            author=author,
            content= request.data["content"]
        )
        serializer = CommentSerializer(comment)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def destroy(self, request, pk):
        comment = Comment.objects.get(pk=pk)
        comment.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)


class CommentAuthorSerializer(serializers.ModelSerializer):
    """JSON serializer for author of comment"""
    class Meta:
        model = RareUser
        fields = ('id', 'user', 'bio', 'profile_image_url', 'active', 'full_name')

class CommentPostSerializer(serializers.ModelSerializer):
    """JSON serializer for post associated with this comment"""
    class Meta:
        model = Post
        fields = ('id', 'user', 'category', 'title', 'publication_date', 'image_url', 'content', 'approved')

class CommentSerializer(serializers.ModelSerializer):
    """JSON serializer for comments"""
    author = CommentAuthorSerializer(many=False)
    post = CommentPostSerializer(many=False)
    class Meta:
        model = Comment
        fields = ('id', 'post', 'author', 'content', 'created_on')

