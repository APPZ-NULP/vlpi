from enum import Enum, auto

from django.contrib.auth.models import User
from django.db import models


class TaskDifficulty(Enum):
    EASY = auto()
    MEDIUM = auto()
    HARD = auto()


class TaskType(Enum):
    USE_CASE = "Use Case"
    SEQUENCE = "Sequence"
    COMMUNICATION = "Communication"
    ACTIVITY = "Activity"
    CLASS = "Class"
    OBJECT = "Object"
    PACKAGE = "Package"
    INTERNAL_STRUCTURE = "Internal Structure"
    COMPONENT = "Component"
    DEPLOYMENT = "Deployment"


class Task(models.Model):
    title = models.CharField("Task title", max_length=512, null=True, blank=True)
    description = models.CharField(
        "Task description", max_length=1024, null=True, blank=True
    )
    difficulty = models.CharField(
        "Task difficulty",
        max_length=50,
        choices=[(difficulty.name, difficulty.name) for difficulty in TaskDifficulty],
        default=TaskDifficulty.EASY.name,
    )
    type = models.CharField(
        "Task type",
        max_length=50,
        choices=[(task_type.name, task_type.value) for task_type in TaskType],
        null=True,
        blank=True,
    )
    max_mark = models.DecimalField(
        max_digits=6, decimal_places=2, null=True, blank=True
    )
    module = models.ForeignKey(
        "modules.StudyingModule",
        on_delete=models.CASCADE,
        related_name="tasks",
        null=True,
        blank=True,
    )
    etalon = models.ForeignKey(
        "etalons.Etalon",
        on_delete=models.CASCADE,
        related_name="etalons",
        null=True,
        blank=True,
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class UserTaskProgress(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="tasks_progress"
    )
    task = models.ForeignKey(
        Task, on_delete=models.CASCADE, related_name="users_progress"
    )
    is_completed = models.BooleanField(null=True, blank=True)
    mark = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.task.title} {self.user.username}"
