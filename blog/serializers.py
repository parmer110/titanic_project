from rest_framework import serializers
from .models import Blog, Post
class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = '__all__'
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'