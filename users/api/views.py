from rest_framework.generics import ListAPIView

from users.models import MaralUser
from users.serializers import UserSerializer


class UserListView(ListAPIView):
    serializer_class = UserSerializer
    queryset = MaralUser.objects.all()