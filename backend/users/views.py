from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from  users.models import User


class ListUsers(APIView):
    """
    View to list all users in the system.

    * Requires token authentication.
    * Only admin users are able to access this view.
    """
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAdminUser]

    def get(self, request, format=None):
        """
        Return a list of all users.
        """
        usernames = [user.name for user in User.objects.all()]
        return Response(usernames)


list_users = ListUsers.as_view()
