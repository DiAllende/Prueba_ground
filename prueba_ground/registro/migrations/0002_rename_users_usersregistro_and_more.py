# Generated by Django 4.1.2 on 2023-06-22 01:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registro', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Users',
            new_name='UsersRegistro',
        ),
        migrations.AlterModelOptions(
            name='usersregistro',
            options={'ordering': ['created'], 'verbose_name': 'User Registrado', 'verbose_name_plural': 'Users registrados'},
        ),
    ]
