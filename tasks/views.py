from django.contrib.auth.models import User
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .filters import TaskFilter
from .models import Task, UserTaskProgress
from .serializers import TaskSerializer, UserTaskProgressSerializer


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    lookup_field = "pk"
    filterset_class = TaskFilter

    @action(detail=True, methods=["post"])
    def complete(self, request, **kwargs):
        # input:
        # - user_id
        # - task_result = {'nodes': [], 'links': [], ...}
        task = self.get_object()

        data = request.data
        user_id = data.get("user_id")
        user_result = data.get("task_result")
        if (
            not user_id
            or not user_result
            or user_result.get("nodes") is None
            or user_result.get("links") is None
        ):
            return Response(
                data={"error": "Payload is incorrect"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        user = User.objects.filter(id=user_id).first()
        if not user:
            return Response(
                data={"error": "User doesn't exist"}, status=status.HTTP_400_BAD_REQUEST
            )

        task_progress = task.users_progress.filter(user=user).first()
        if not task_progress:
            return Response(
                data={"error": "Given user didn't start completing task"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        result_mark = self.evaluate_result_mark(
            task.etalon, user_result, float(task.max_mark)
        )
        task_progress.mark = result_mark
        task_progress.is_completed = True
        task_progress.nodes = user_result.get("nodes")
        task_progress.links = user_result.get("links")
        task_progress.save()

        return Response(status=status.HTTP_200_OK)

    def evaluate_result_mark(self, etalon, result, max_mark):
        etalon_links = list(
            map(
                lambda link: {"from": link["from"], "to": link["to"]},
                etalon.links,
            )
        )
        result_links = list(
            map(
                lambda link: {"from": link["from"], "to": link["to"]},
                result["links"],
            )
        )

        etalon_links_copy = etalon_links[:]
        result_links_copy = result_links[:]

        for link in result_links:
            if link in etalon_links:
                etalon_links_copy.remove(link)
                result_links_copy.remove(link)

        original_size = len(etalon_links) + len(result_links)
        copy_size = len(etalon_links_copy) + len(result_links_copy)

        mistakes_procent = copy_size / original_size

        mark = max_mark * (1 - mistakes_procent)
        return mark


class UserTaskProgressViewSet(viewsets.ModelViewSet):
    queryset = UserTaskProgress.objects.all()
    serializer_class = UserTaskProgressSerializer
    lookup_field = "pk"


# {
#     "links": [
#         {"key": -1, "from": 0, "to": 1},
#         {"key": -2, "from": 0, "to": 2},
#         {"key": -3, "from": 1, "to": 1},
#         {"key": -4, "from": 2, "to": 3},
#         {"key": -5, "from": 3, "to": 0},
#     ]
# }
# {
#     "links": [
#         {"key": -1, "from": 0, "to": 1},
#         {"key": -2, "from": 0, "to": 2},
#         {"key": -5, "from": 3, "to": 0},
#     ]
# }
# {
#     "links": [
#         {"key": -1, "from": 0, "to": 1},
#         {"key": -2, "from": 0, "to": 2},
#         {"key": -3, "from": 1, "to": 1},
#         {"key": -4, "from": 2, "to": 3},
#         {"key": -5, "from": 3, "to": 0},
#         {"key": -6, "from": 0, "to": 3},
#         {"key": -7, "from": 0, "to": 4},
#     ]
# }
