# Generated by Django 5.1.2 on 2024-11-27 01:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gym', '0009_remove_trainner_bmr'),
    ]

    operations = [
        migrations.AddField(
            model_name='trainner',
            name='bmr',
            field=models.DecimalField(decimal_places=5, max_digits=10, null=True, verbose_name='bmr'),
        ),
    ]