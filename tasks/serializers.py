from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Task, UserTaskProgress


class FilteredListSerializer(serializers.ListSerializer):
    def to_representation(self, data):
        request = self.context["request"]
        user_id = request.query_params.get("user")
        if user_id:
            user = User.objects.filter(id=user_id).first()
            if not user:
                return
            if not user.is_superuser:
                data = data.filter(user=user)
        return super(FilteredListSerializer, self).to_representation(data)


class UserTaskProgressSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserTaskProgress
        fields = ["pk", "user", "task", "is_completed", "created_at", "updated_at"]
        list_serializer_class = FilteredListSerializer


class TaskSerializer(serializers.ModelSerializer):
    users_progress = UserTaskProgressSerializer(many=True)

    class Meta:
        model = Task
        fields = [
            "pk",
            "title",
            "description",
            "difficulty",
            "type",
            "module",
            "users_progress",
            "created_at",
            "updated_at",
        ]
