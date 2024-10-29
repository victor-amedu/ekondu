from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from.models import Blog
from.serializers import BlogSerializers

# Create your views here.
class BlogViewset(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Blog.objects.all()
    serializer_class = BlogSerializers
    @action(detail=True, methods=["post"])
    def like(self, request, pk=None):
        Blog = self.get_object()
        return Response({"status" : "blog liked"})