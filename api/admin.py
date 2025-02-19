from django.contrib import admin
from .models import DayClass, Interval, Subject,Job,Topic

# Register your models here.

admin.site.register(DayClass)
admin.site.register(Interval)
admin.site.register(Subject)
admin.site.register(Job)
admin.site.register(Topic)
