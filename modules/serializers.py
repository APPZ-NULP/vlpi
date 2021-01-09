from rest_framework import serializers

from .models import StudyingModule


class StudyingModuleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = StudyingModule
        fields = ["pk", "name"]
