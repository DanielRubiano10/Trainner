# Generated by Django 5.1.2 on 2024-11-26 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Trainner',
            fields=[
                ('id_persona', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100, verbose_name='nombre')),
                ('sexo', models.CharField(max_length=50, verbose_name='sexo')),
                ('edad', models.IntegerField(verbose_name='edad')),
                ('peso', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='peso')),
                ('altura', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='altura')),
                ('cintura', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='cintura')),
                ('cuello', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='cuello')),
                ('cadera', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='cadera')),
            ],
        ),
    ]
