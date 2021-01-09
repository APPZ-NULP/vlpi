import django_filters

from .models import Task


class TaskFilter(django_filters.FilterSet):
    user = django_filters.CharFilter(field_name="home__uid")

    class Meta:
        model = Task
        fields = []
