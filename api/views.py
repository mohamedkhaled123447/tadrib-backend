from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializers import (
    DayCalssSerializer,
    IntervalSerializer,
    IntervalListSerializer,
    SubjectSerializer,
    JobSerializer,
    TopicSerializer,
)
from .models import DayClass, Interval, Subject, Job, Topic
from rest_framework.response import Response
from rest_framework.views import APIView
from .print import generate_545_doc

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


class TopicViewSet(ModelViewSet):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer


class JobViewSet(ModelViewSet):
    queryset = Job.objects.all()
    serializer_class = JobSerializer


class Doc545(APIView):
    def post(self, request, *args, **kwargs):
        generate_545_doc(
            request.data["data"],
            request.data["subjects"],
            request.data["len"],
            request.data["week"],
            request.data["month"],
            request.data["totalTrainingHours"],
            request.data["totalBoundEducationHours"],
            request.data["start"],
            request.data["end"],
        )
        return Response("ok")
