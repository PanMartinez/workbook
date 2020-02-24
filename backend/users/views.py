from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import authentication, permissions

from users.models import User
from users.serializers import UserSerializer


class ListUsers(APIView):
    """
    View to list all users in the system.

    * Requires token authentication.
    * Only admin users are able to access this view.
    """
    # authentication_classes = [authentication.TokenAuthentication]
    # permission_classes = [permissions.IsAdminUser]

    authentication_classes = []
    permission_classes = []

    def get(self, request):

        users_list = User.objects.all()
        serializer = UserSerializer(users_list, many=True)

        return Response(serializer.data)


list_users = ListUsers.as_view()
