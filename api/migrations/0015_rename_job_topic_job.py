# Generated by Django 5.1 on 2025-02-16 23:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0014_topic_job_alter_topic_instructor_alter_topic_place_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='topic',
            old_name='Job',
            new_name='job',
        ),
    ]
