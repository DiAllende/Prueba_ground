# Generated by Django 4.1.2 on 2023-06-21 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0003_alter_users_nombre_alter_users_pais_alter_users_rut'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='admin',
            field=models.BooleanField(default=False, verbose_name='Administrador'),
        ),
    ]
