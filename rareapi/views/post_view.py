from django.http import HttpResponseServerError
from django.contrib.auth.models import User
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from rareapi.models import Post, RareUser, Category



class PostView(ViewSet):

    def retrieve(self, request, pk):
        post = Post.objects.get(pk=pk)
        serializer = PostSerializer(post)
        return Response(serializer.data)

    def list(self, request):
        posts = []
        if "approved" in request.query_params:
            approved_post = request.query_params['approved'] 
        
            if request.auth.user.is_staff:
                posts = Post.objects.order_by('publication_date')
            else:
                posts = Post.objects.filter(rare_user=request.auth.user and approved_post == True).order_by('publication_date')
        else: 
            posts = Post.objects.order_by('publication_date')


            
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
            title= request.data["title"],
            publication_date=request.data["publication_date"],
            image_url=request.data["image_url"],
            content=request.data["content"],
            approved=request.data["approved"]




        )
        serializer = PostSerializer(post)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class RareUserSerializer(serializers.ModelSerializer):
  
    class Meta:
        model = RareUser
        fields = ('id', 'user', 'bio', 'profile_image_url', 'created_on', 'active')

class CategorySerializer(serializers.ModelSerializer):
    """JSON serializer for categories"""
    class Meta:
        model = Category
        fields = ('id', 'label')


class PostSerializer(serializers.ModelSerializer):
    
    category = CategorySerializer(many=False)
    user = RareUserSerializer(many=False)
    class Meta:
        model = Post
        fields = ('id', 'user', 'category', 'title', 'publication_date', 'image_url', 'content', 'approved')


