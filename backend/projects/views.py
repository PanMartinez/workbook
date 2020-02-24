from rest_framework.generics import ListCreateAPIView

from users.permissions import IsManager

from projects.models import Project
from projects.serializers import ProjectSerializer


class ProjectsListView(ListCreateAPIView):
    """
    view for admin to manage all projects in company
    """
    # permission_classes = [IsManager]
    permission_classes = []

    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


projects_list = ProjectsListView.as_view()
