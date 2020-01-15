from rest_framework.views import APIView

from .models import WorkDay
from .serializers import WorkDaySerializer


class WorkbooksListView(APIView):
    """
    View with all workbook for current user
    """
    def get(self, request):
        user = request['user']

        workbook_list = WorkDay.objects.filter(user=user).list()



