from django.db import models


class Project(models.Model):
    name = models.CharField('name of the project', max_length=32, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Project"
        verbose_name_plural = "Projects"
