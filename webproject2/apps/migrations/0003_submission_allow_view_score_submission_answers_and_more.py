# Generated by Django 5.0.5 on 2024-06-03 01:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0002_alter_class_students'),
    ]

    operations = [
        migrations.AddField(
            model_name='submission',
            name='allow_view_score',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='submission',
            name='answers',
            field=models.JSONField(default=dict),
        ),
        migrations.AddField(
            model_name='submission',
            name='pcap_file',
            field=models.FileField(blank=True, null=True, upload_to='pcap_files/'),
        ),
        migrations.AddField(
            model_name='submission',
            name='score',
            field=models.IntegerField(default=0),
        ),
    ]
