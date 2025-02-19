# Generated by Django 5.1 on 2025-02-16 23:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0013_rename_teacher_topic_instructor_topic_level_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='topic',
            name='Job',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='job_topics', to='api.job'),
        ),
        migrations.AlterField(
            model_name='topic',
            name='instructor',
            field=models.CharField(default='لايكن', max_length=250),
        ),
        migrations.AlterField(
            model_name='topic',
            name='place',
            field=models.CharField(default='لايكن', max_length=250),
        ),
        migrations.AlterField(
            model_name='topic',
            name='subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subject_topics', to='api.subject'),
        ),
        migrations.AlterField(
            model_name='topic',
            name='training_tools',
            field=models.CharField(default='لايكن', max_length=250),
        ),
    ]
