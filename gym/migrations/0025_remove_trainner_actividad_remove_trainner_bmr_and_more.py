# Generated by Django 5.0.6 on 2024-11-27 04:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gym', '0024_alter_trainner_calorias'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trainner',
            name='actividad',
        ),
        migrations.RemoveField(
            model_name='trainner',
            name='bmr',
        ),
        migrations.RemoveField(
            model_name='trainner',
            name='calorias',
        ),
        migrations.RemoveField(
            model_name='trainner',
            name='imc',
        ),
        migrations.RemoveField(
            model_name='trainner',
            name='indice_cintura',
        ),
        migrations.RemoveField(
            model_name='trainner',
            name='masa_corporal',
        ),
        migrations.RemoveField(
            model_name='trainner',
            name='porcen_graso',
        ),
    ]
