from rest_framework import viewsets

from .models import StudyingModule
from .serializers import StudyingModuleSerializer


class StudyingModuleViewSet(viewsets.ModelViewSet):
    queryset = StudyingModule.objects.all()
    serializer_class = StudyingModuleSerializer
    lookup_field = "pk"
