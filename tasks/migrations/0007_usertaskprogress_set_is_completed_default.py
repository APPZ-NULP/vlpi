# Generated by Django 3.1.5 on 2021-01-10 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0006_task_add_max_mark'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usertaskprogress',
            name='is_completed',
            field=models.BooleanField(default=False),
        ),
    ]
