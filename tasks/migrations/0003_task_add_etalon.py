# Generated by Django 3.1.5 on 2021-01-10 12:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('etalons', '0001_add_etalon'),
        ('tasks', '0002_task_add_module'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='etalon',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='etalons', to='etalons.etalon'),
        ),
    ]
