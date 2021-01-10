from django.db import models


class Etalon(models.Model):
    nodes = models.JSONField(null=True, blank=True)
    links = models.JSONField(null=True, blank=True)
