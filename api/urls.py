from django.urls import path, include
from .views import DayClassViewSet, IntervalViewSet, SubjectViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"day-class", DayClassViewSet, basename="day_class")
router.register(r"interval", IntervalViewSet, basename="interval")
router.register(r"subject", SubjectViewSet, basename="subject")
urlpatterns = [path("", include(router.urls))]
