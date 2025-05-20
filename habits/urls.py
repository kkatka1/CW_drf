from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import HabitViewSet, PublicHabitListAPIView

app_name = "habits"

router = DefaultRouter()
router.register(r"", HabitViewSet, basename="habit")

urlpatterns = [
    path("public/", PublicHabitListAPIView.as_view(), name="public-habits"),
]
urlpatterns += router.urls
