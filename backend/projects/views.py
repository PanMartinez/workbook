from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import IsAdminUser

from projects.models import Project
from projects.serializers import ProjectSerializer


class ProjectsListView(ListCreateAPIView):
    """
    view for admin to manage all projects in company
    """
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [IsAdminUser]


projects_list = ProjectsListView.as_view()
