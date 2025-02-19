from django.urls import path, include
from .views import (
    DayClassViewSet,
    IntervalViewSet,
    SubjectViewSet,
    Doc545,
    JobViewSet,
    TopicViewSet,
)
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"day-class", DayClassViewSet, basename="day_class")
router.register(r"interval", IntervalViewSet, basename="interval")
router.register(r"subject", SubjectViewSet, basename="subject")
router.register(r"topic", TopicViewSet, basename="topic")
router.register(r"job", JobViewSet, basename="job")
urlpatterns = [path("", include(router.urls)), path("545/", Doc545.as_view())]
