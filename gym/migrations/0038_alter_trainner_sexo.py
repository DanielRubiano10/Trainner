# Generated by Django 5.0.6 on 2024-11-27 22:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gym', '0037_remove_trainner_bmr'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trainner',
            name='sexo',
            field=models.CharField(choices=[('1', 'Hombre'), ('2', 'Mujer')], max_length=50, verbose_name='sexo'),
        ),
    ]
