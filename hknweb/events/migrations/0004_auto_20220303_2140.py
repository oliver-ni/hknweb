# Generated by Django 2.2.8 on 2022-03-04 05:40

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('events', '0003_gcalaccesslevelmapping'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='rsvp',
            unique_together={('user', 'event')},
        ),
    ]