# Generated by Django 5.0.5 on 2024-06-20 01:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0009_rename_is_submited_submission_is_submitted'),
    ]

    operations = [
        migrations.RenameField(
            model_name='submission',
            old_name='assignment_id',
            new_name='assignment',
        ),
    ]