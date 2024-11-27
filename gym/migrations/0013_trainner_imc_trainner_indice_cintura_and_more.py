# Generated by Django 5.1.2 on 2024-11-27 01:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gym', '0012_alter_trainner_bmr'),
    ]

    operations = [
        migrations.AddField(
            model_name='trainner',
            name='imc',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True, verbose_name='imc'),
        ),
        migrations.AddField(
            model_name='trainner',
            name='indice_cintura',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True, verbose_name='indice_cintura'),
        ),
        migrations.AlterField(
            model_name='trainner',
            name='actividad',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='actividad'),
        ),
        migrations.AlterField(
            model_name='trainner',
            name='altura',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='altura'),
        ),
        migrations.AlterField(
            model_name='trainner',
            name='bmr',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, verbose_name='bmr'),
        ),
        migrations.AlterField(
            model_name='trainner',
            name='cadera',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='cadera'),
        ),
        migrations.AlterField(
            model_name='trainner',
            name='cintura',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='cintura'),
        ),
        migrations.AlterField(
            model_name='trainner',
            name='cuello',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='cuello'),
        ),
        migrations.AlterField(
            model_name='trainner',
            name='peso',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='peso'),
        ),
    ]
