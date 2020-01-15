from django.db import models

from projects.models import Project

from users.models import User


class Day(models.Model):
    date = models.DateField()


class WorkDay(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, null=True, blank=True)
    day = models.ForeignKey(Day, on_delete=models.CASCADE, null=True, blank=True)
    duration = models.DurationField(null=True, blank=True)
    description = models.CharField('Tasks description', max_length=256, null=True, blank=True)



