from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from users.serializers import RegisterSerializer
from users.models import User


class UserCreateAPIView(CreateAPIView):
    """Регистрация пользователя"""

    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]
