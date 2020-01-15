from django.db import models


class Project(models.Model):
    name = models.CharField('name of the project', max_length=32, null=True, blank=True)

