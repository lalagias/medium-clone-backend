from django.contrib.auth.models import User, Group
from .models import Post, Profile, Comment, Tag

from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name', 'last_name',
                  'groups')


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')


class ProfileSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', )
    first_name = serializers.CharField(source='user.first_name', )
    last_name = serializers.CharField(source='user.last_name', )

    class Meta:
        model = Profile
        fields = ('user', 'username', 'first_name', 'last_name', 'bio',
                  'image')
        read_only_fields = (
            'username',
            'first_name',
            'last_name',
        )


class PostSerializer(serializers.ModelSerializer):
    author = ProfileSerializer(read_only=True)

    class Meta:
        model = Post
        fields = (
            'id',
            'author',
            'title',
            'description',
            'text',
            'created_date',
            'image',
        )
        # depth = 1


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'post', 'author', 'text', 'created_date')
        depth = 1


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('tag')