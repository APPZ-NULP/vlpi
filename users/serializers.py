from django.contrib.auth.models import User
from rest_framework import serializers

from .models import UserType


class UserSerializer(serializers.HyperlinkedModelSerializer):
    type = serializers.SerializerMethodField()

    def get_type(self, user):
        if user.is_superuser:
            return UserType.ADMIN.name
        return UserType.STUDENT.name

    class Meta:
        model = User
        fields = [
            "pk",
            "username",
            "first_name",
            "last_name",
            "email",
            "type",
            "is_superuser",
        ]
