# Generated by Django 5.0.6 on 2024-11-27 04:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gym', '0032_trainner_actividad'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trainner',
            name='actividad',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='actividad'),
        ),
    ]