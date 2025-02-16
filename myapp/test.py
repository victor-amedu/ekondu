from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Blog

class BlogTests(APITestCase):
    def test_create_blog(self):
        """
        Ensure we can create a new blog post."""
        url = reverse('blog-list')
        data = {'title': 'Test Post', 'content': 'Test content'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Blog.objects.count(), 1)
        self.assertEqual(Blog.objects.get().title, 'Test Post')
