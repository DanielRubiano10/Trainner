# Generated by Django 5.1.2 on 2024-11-27 01:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gym', '0019_trainner_masa_corporal'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trainner',
            name='masa_corporal',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, verbose_name='masa_corporal'),
        ),
    ]
