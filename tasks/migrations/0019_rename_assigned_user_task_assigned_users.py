# Generated by Django 4.2.6 on 2023-12-11 17:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0018_remove_task_assigned_user_task_assigned_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='assigned_user',
            new_name='assigned_users',
        ),
    ]
