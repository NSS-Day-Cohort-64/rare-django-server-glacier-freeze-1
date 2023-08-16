from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status

class CategoryView(ViewSet):
    """category views"""

    def list(self, request):
        """handles GET requests to return a list of categories"""