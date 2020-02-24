from django.db import models

from projects.models import Project

from users.models import User


class WorkDay(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, null=True, blank=True)
    day = models.DateField('Day of work', null=True, blank=True)
    duration = models.DurationField(null=True, blank=True)
    description = models.CharField('Tasks description', max_length=256, null=True, blank=True)

    def __str__(self):
        return self.day.strftime('%x')

    class Meta:
        verbose_name = "Work Day"
        verbose_name_plural = "Work Days"
