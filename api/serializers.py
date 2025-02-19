from rest_framework.serializers import ModelSerializer
from .models import DayClass, Interval, Subject, Job, Topic


class DayCalssSerializer(ModelSerializer):
    class Meta:
        model = DayClass
        fields = "__all__"


class IntervalSerializer(ModelSerializer):
    class Meta:
        model = Interval
        fields = "__all__"


class IntervalListSerializer(ModelSerializer):
    class Meta:
        model = Interval
        fields = ["id", "name"]


class TopicSerializer(ModelSerializer):
    class Meta:
        model = Topic
        fields = "__all__"


class SubjectSerializer(ModelSerializer):
    class Meta:
        model = Subject
        fields = "__all__"


class JobSerializer(ModelSerializer):
    class Meta:
        model = Job
        fields = "__all__"
