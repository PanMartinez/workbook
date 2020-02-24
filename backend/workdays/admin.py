from django.contrib import admin

from workdays.models import WorkDay


@admin.register(WorkDay)
class WorkDayAdmin(admin.ModelAdmin):
    pass

