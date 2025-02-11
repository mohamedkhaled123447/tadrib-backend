from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializers import (
    DayCalssSerializer,
    IntervalSerializer,
    IntervalListSerializer,
    SubjectSerializer,
)
from .models import DayClass, Interval, Subject
from rest_framework.response import Response

# Create your views here.


class DayClassViewSet(ModelViewSet):
    queryset = DayClass.objects.all()
    serializer_class = DayCalssSerializer


class IntervalViewSet(ModelViewSet):
    queryset = Interval.objects.all()
    serializer_class = IntervalSerializer

    def list(self, request, *args, **kwargs):
        intervals = Interval.objects.only("id", "name").all()
        return Response(IntervalListSerializer(intervals, many=True).data)


class SubjectViewSet(ModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
