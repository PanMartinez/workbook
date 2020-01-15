from rest_framework import serializers

from .models import WorkDay


class WorkDaySerializer(serializers.ModelSerializer):

    class Meta:
        model = WorkDay
        fields = '__all__'

