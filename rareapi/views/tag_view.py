from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from rareapi.models import Tag


class TagView(ViewSet):

    def retrieve(self, request, pk):
        tag = Tag.objects.get(pk=pk)
        serializer = TagSerializer(tag)
        return Response(serializer.data)

    def list(self, request):
        tags = Tag.objects.order_by('label')
        serializer = TagSerializer(tags, many=True)
        return Response(serializer.data)

    def update(self, request, pk):
        """handles PUT requests for updating a category"""
        tag = Tag.objects.get(pk=pk)
        tag.label = request.data['label']

        tag.save()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk):
        tag = Tag.objects.get(pk=pk)
        tag.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
    
    def create(self, request):
        """Handle POST operations """

        tag = Tag.objects.create(
            label=request.data["label"],
        )
        serializer = TagSerializer(tag)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class TagSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tag
        fields = ('id', 'label')
