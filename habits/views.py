from rest_framework.generics import ListAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, AllowAny

from users.permissions import IsOwnerOrPublicReadOnly
from .models import Habit
from .paginations import HabitPagination
from .serializers import HabitSerializer


class HabitViewSet(ModelViewSet):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrPublicReadOnly]
    pagination_class = HabitPagination


    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class PublicHabitListAPIView(ListAPIView):
    """Список публичных привычек (read-only)"""

    queryset = Habit.objects.filter(is_public=True)
    serializer_class = HabitSerializer
    permission_classes = [AllowAny]
    pagination_class = HabitPagination
