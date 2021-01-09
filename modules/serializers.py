from django.contrib.auth.models import User
from rest_framework import serializers

from .models import StudyingModule


class StudyingModuleSerializer(serializers.HyperlinkedModelSerializer):
    tasks_all = serializers.SerializerMethodField()
    tasks_done = serializers.SerializerMethodField()
    tasks_in_progress = serializers.SerializerMethodField()

    def get_tasks_all(self, module):
        return module.all_tasks_count

    def get_user(self):
        user = None
        request = self.context["request"]
        user_id = request.query_params.get("user")
        if user_id:
            user = User.objects.filter(id=user_id).first()
        return user

    def get_tasks_done(self, module):
        # should be request.user
        user = self.get_user()
        if not user:
            return 0

        if user.is_superuser:
            result = module.all_tasks_count
        else:
            result = module.get_done_tasks_count(user)

        return result

    def get_tasks_in_progress(self, module):
        # should be request.user
        user = self.get_user()
        if not user:
            return 0

        if user.is_superuser:
            result = 0
        else:
            result = module.get_in_progress_tasks_count(user)

        return result

    class Meta:
        model = StudyingModule
        fields = ["pk", "name", "tasks_all", "tasks_done", "tasks_in_progress"]
