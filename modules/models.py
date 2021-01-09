from django.db import models


class StudyingModule(models.Model):
    name = models.CharField("Module name", max_length=512, null=True, blank=True)

    def __str__(self):
        return self.name


#  TODO properties + serializer fields (all_tasks_count, done_tasks_count, in_progress_tasks_count)
