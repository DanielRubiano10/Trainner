# Generated by Django 5.1.2 on 2024-11-27 01:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gym', '0016_alter_trainner_masa_corporal_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trainner',
            name='masa_corporal',
        ),
    ]