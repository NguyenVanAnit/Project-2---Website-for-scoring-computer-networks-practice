# Generated by Django 5.0.5 on 2024-06-02 15:30

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='class',
            name='students',
            field=models.ManyToManyField(limit_choices_to={'role': 0}, related_name='classes_enrolled', to=settings.AUTH_USER_MODEL),
        ),
    ]
