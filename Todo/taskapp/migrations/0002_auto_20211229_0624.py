# Generated by Django 2.2.12 on 2021-12-29 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='status',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='created_date',
            field=models.DateField(default='2021-12-29'),
        ),
    ]
