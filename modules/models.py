from django.db import models

from tasks.models import Task, UserTaskProgress


class StudyingModule(models.Model):
    name = models.CharField("Module name", max_length=512, null=True, blank=True)

    def __str__(self):
        return self.name

    @property
    def all_tasks_count(self):
        return self.tasks.count()

    def get_done_tasks_count(self, user):
        module_tasks = self.tasks.all()
        done_tasks_progresses = UserTaskProgress.objects.filter(
            user=user, is_completed=True, task__in=module_tasks
        )
        done_tasks = Task.objects.filter(users_progress__in=done_tasks_progresses)
        return done_tasks.count()

    def get_in_progress_tasks_count(self, user):
        module_tasks = self.tasks.all()
        in_progress_tasks_progresses = UserTaskProgress.objects.filter(
            user=user, is_completed=False, task__in=module_tasks
        )
        in_progress_tasks = Task.objects.filter(
            users_progress__in=in_progress_tasks_progresses
        )
        return in_progress_tasks.count()
