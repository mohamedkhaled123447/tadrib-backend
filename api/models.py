from django.db import models
from .utils import default_interval, default_months_data, default_types, default_jobs


class DayClass(models.Model):
    name = models.CharField(max_length=100, default="")
    color = models.CharField(max_length=100, default="")
    trainingHours = models.IntegerField(default=0)
    dayLearningHours = models.IntegerField(default=0)
    nightLearningHours = models.IntegerField(default=0)
    boundEducationHours = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Interval(models.Model):
    name = models.CharField(max_length=150, default="")
    data = models.JSONField(default=default_interval)
    monthsData = models.JSONField(default=default_months_data)
    types = models.JSONField(default=default_types)
    weekStart = models.IntegerField(default=1)

    def __str__(self):
        return self.name


class Subject(models.Model):
    name = models.CharField(max_length=150)
    type = models.IntegerField()
    persentage = models.IntegerField()
    day = models.BooleanField()
    night = models.BooleanField()

    def __str__(self):
        return self.name


class Job(models.Model):
    name = models.CharField(max_length=150)
    subjects = models.JSONField(default=default_jobs)


class Topic(models.Model):
    name = models.CharField(max_length=150)
    place = models.CharField(max_length=250, default="لايكن")
    training_tools = models.CharField(max_length=250, default="لايكن")
    instructor = models.CharField(max_length=250, default="لايكن")
    day = models.BooleanField(default=True)
    night = models.BooleanField(default=False)
    level = models.IntegerField(default=0)
    topic_class = models.CharField(max_length=150, default="فرد")
    job = models.ForeignKey(
        Job, related_name="job_topics", on_delete=models.SET_NULL, null=True, blank=True
    )
    subject = models.ForeignKey(
        Subject,
        on_delete=models.CASCADE,
        related_name="subject_topics",
        null=True,
        blank=True,
    )
