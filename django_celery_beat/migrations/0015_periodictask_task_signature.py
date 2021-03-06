# Generated by Django 2.2.16 on 2020-09-01 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_celery_beat', '0014_remove_clockedschedule_enabled'),
    ]

    operations = [
        migrations.AddField(
            model_name='periodictask',
            name='task_signature',
            field=models.BinaryField(help_text="Serialized `celery.canvas.Signature` type's object of task (or chain, group, etc.) got by https://pypi.org/project/dill/", null=True),
        ),
        migrations.AddField(
            model_name='periodictask',
            name='task_signature_sign',
            field=models.CharField(help_text="Signature (in hex) of serialized `celery.canvas.Signature` type's object (see task_signature field)", max_length=1028, null=True),
        ),
    ]
