# Generated by Django 2.2.4 on 2019-08-30 00:46
# flake8: noqa
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('django_celery_beat', '0013_auto_20200609_0727'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='clockedschedule',
            name='enabled',
        ),
    ]