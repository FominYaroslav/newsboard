from rest_framework import serializers
from newsapp.models import User, News, Comment
from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow author of an object to edit it.
    """

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions are only allowed to the author of content
        return obj.author == request.user


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("username", "is_staff")


class NewsSerializer(serializers.ModelSerializer):
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    class Meta:
        model = News
        fields = (
            "id",
            "title",
            "link",
            "creation_date",
            "amount_of_upvotes",
            "author",
            "amount_of_upvotes",
        )
        read_only_fields = ("author",)


class CommentSerializer(serializers.ModelSerializer):
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    class Meta:
        model = Comment
        fields = ("id", "author", "news", "content", "creation_date")
        read_only_fields = ("author",)
