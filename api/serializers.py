from rest_framework.serializers import ModelSerializer
from .models import DayClass, Interval, Subject


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


class SubjectSerializer(ModelSerializer):
    class Meta:
        model = Subject
        fields = "__all__"
