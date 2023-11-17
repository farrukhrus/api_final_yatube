from rest_framework import serializers
from rest_framework.generics import get_object_or_404
from django.db import models

from posts.models import Post, Group, Comment, Follow, User


class PostSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        slug_field='username',
        read_only=True)

    class Meta:
        model = Post
        fields = ('id', 'text', 'author', 'pub_date', 'image', 'group')


class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = Group
        fields = ('id', 'title', 'slug', 'description')


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username'
    )

    class Meta:
        model = Comment
        fields = ('id', 'author', 'post', 'text', 'created')
        read_only_fields = ('post',)


class FollowSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(slug_field='username', read_only=True)
    following = serializers.SlugRelatedField(slug_field='username',
                                             queryset=User.objects.all())

    def validate(self, data):
        user = get_object_or_404(User, username=data['following'].username)
        isFollowing = Follow.objects.filter(user=self.context['request'].user,
                                            following=user).exists()
        if user == self.context['request'].user:
            raise serializers.ValidationError(
                "Вы не можете подписаться на себя")
        if isFollowing:
            raise serializers.ValidationError(
                "Вы уже подписаны на этого пользователя")
        return data

    class Meta:
        model = Follow
        fields = ('user', 'following')

        constraints = [
            models.UniqueConstraint(
                fields=['user', 'following'], name='no_self_following'
            ),
        ]
