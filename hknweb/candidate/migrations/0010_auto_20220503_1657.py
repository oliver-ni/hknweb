# Generated by Django 2.2.8 on 2022-05-03 23:57

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('candidate', '0009_auto_20220503_1641'),
    ]

    operations = [
        migrations.AlterField(
            model_name='externalreq',
            name='completed',
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL),
        ),
    ]
