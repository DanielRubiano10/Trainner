# Generated by Django 5.0.6 on 2024-11-27 05:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gym', '0036_alter_trainner_bmr'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trainner',
            name='bmr',
        ),
    ]