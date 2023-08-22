from django.http import HttpResponseServerError
from django.contrib.auth.models import User
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from rareapi.models import Post, RareUser, Category, Tag, Comment, Reaction


class PostView(ViewSet):

    def retrieve(self, request, pk):
        post = Post.objects.get(pk=pk)
        serializer = PostSerializer(post)
        return Response(serializer.data)

    def list(self, request):
        posts = Post.objects.filter(user__active=True).order_by('-publication_date')
        if "approved" in request.query_params and request.query_params['approved'] == 'true':
            posts = posts.filter(approved = True)
        elif "approved" in request.query_params and request.query_params['approved'] == 'false':
            posts = posts.filter(approved = False)
        elif "user" in request.query_params:
            pk= request.query_params['user']
            posts = posts.filter(user = pk)
    
    
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

    



    def destroy(self, request, pk):
        post = Post.objects.get(pk=pk)
        post.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def create(self, request):
        """Handle POST operations """
        user = RareUser.objects.get(pk=request.data["user"])
        category = Category.objects.get(pk=request.data["category"])

        post = Post.objects.create(
            user=user,
            category=category,
            title=request.data["title"],
            image_url=request.data["image_url"],
            content=request.data["content"],
            approved=request.data["approved"]

        )
        serializer = PostSerializer(post)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def update(self, request, pk):
        """handles PUT requests for updating a Comment"""
        post = Post.objects.get(pk=pk)
        post.user = RareUser.objects.get(pk=request.data['user'])
        post.category = Category.objects.get(pk=request.data["category"])
        post.content = request.data["content"]
        post.title = request.data["title"]
        post.publication_date = request.data["publication_date"]
        post.image_url = request.data["image_url"]
        post.approved = request.data["approved"]

        post.save()
        
        new_tag_array= request.data["tags"]
        post.tags.set(new_tag_array)

        return Response(None, status=status.HTTP_204_NO_CONTENT)


class RareUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = RareUser
        fields = ('id', 'user', 'bio', 'profile_image_url',
                  'created_on', 'active', 'full_name')


class CategorySerializer(serializers.ModelSerializer):
    """JSON serializer for categories"""
    class Meta:
        model = Category
        fields = ('id', 'label')

class TagSerializer(serializers.ModelSerializer):
  
        class Meta:
            model = Tag
            fields = ('id','label')

class CommentAuthorSerializer(serializers.ModelSerializer):
    """JSON serializer for author of comment"""
    class Meta:
        model = RareUser
        fields = ('id', 'user', 'bio', 'profile_image_url', 'active', 'full_name')


class CommentSerializer(serializers.ModelSerializer):
    """JSON serializer for comments"""
    author = CommentAuthorSerializer(many=False)
    class Meta:
        model = Comment
        fields = ('id', 'post', 'author', 'content', 'created_on')

class ReactionSerializer(serializers.ModelSerializer):
  
    class Meta:
        model = Reaction
        fields = ('id', 'label', 'image_url')

class PostSerializer(serializers.ModelSerializer):

    category = CategorySerializer(many=False)
    user = RareUserSerializer(many=False)
    tags = TagSerializer(many=True)
    comment_posts = CommentSerializer(many=True)
    reactions = ReactionSerializer(many=True)
    class Meta:
        model = Post
        fields = ('id', 'user', 'category', 'title',
                  'publication_date', 'image_url', 'content', 
                  'approved', 'tags', "comment_posts", "reactions")
