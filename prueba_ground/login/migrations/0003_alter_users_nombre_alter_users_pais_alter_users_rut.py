# Generated by Django 4.1.2 on 2023-06-13 00:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0002_alter_users_options_users_cp_users_direccion_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='nombre',
            field=models.CharField(max_length=200, verbose_name='Nombre completo'),
        ),
        migrations.AlterField(
            model_name='users',
            name='pais',
            field=models.CharField(max_length=100, verbose_name='Pais'),
        ),
        migrations.AlterField(
            model_name='users',
            name='rut',
            field=models.CharField(max_length=200, verbose_name='Rut'),
        ),
    ]
