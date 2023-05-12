from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from posts.models import Comment, Follow, Group, Post


class PostSerializer(ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username',
    )

    class Meta:
        model = Post
        fields = '__all__'


class GroupSerializer(ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'


class FollowSerializer(ModelSerializer):
    user = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username',
    )
    following = serializers.SlugRelatedField(
        queryset=User.objects.all(),
        slug_field='username',
    )

    def validate_following(self, value):
        following = get_object_or_404(User,
                                      username=value
                                      )
        user = self.context['request'].user
        if Follow.objects.filter(
                user=user.id,
                following=following.id).exists() or user == following:
            raise serializers.ValidationError()
        return value

    class Meta:
        model = Follow
        fields = ('user', 'following')


class CommentSerializer(ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username',
    )

    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('post',)
