# Generated by Django 5.1.2 on 2024-11-27 01:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gym', '0011_alter_trainner_bmr'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trainner',
            name='bmr',
            field=models.DecimalField(blank=True, decimal_places=5, max_digits=10, verbose_name='bmr'),
        ),
    ]
