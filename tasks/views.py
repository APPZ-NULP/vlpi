from rest_framework import viewsets

from .models import Task
from .serializers import TaskSerializer


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    lookup_field = "pk"

    # action - complete_task (передають юзера, виконання таски юзером, звіряю і ставлю оцінку)
