# Generated by Django 5.0.5 on 2024-06-17 04:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0004_submission_student_input'),
    ]

    operations = [
        migrations.RenameField(
            model_name='submission',
            old_name='assignment_id',
            new_name='assignment',
        ),
        migrations.RenameField(
            model_name='submission',
            old_name='is_submited',
            new_name='is_submitted',
        ),
    ]
