# Generated by Django 4.1.2 on 2023-06-23 19:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registro', '0003_usersregistro_groups_usersregistro_is_superuser_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usersregistro',
            name='groups',
        ),
        migrations.RemoveField(
            model_name='usersregistro',
            name='is_superuser',
        ),
        migrations.RemoveField(
            model_name='usersregistro',
            name='last_login',
        ),
        migrations.RemoveField(
            model_name='usersregistro',
            name='user_permissions',
        ),
    ]
