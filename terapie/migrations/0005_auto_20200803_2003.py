# Generated by Django 3.0.8 on 2020-08-03 20:03

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('terapie', '0004_auto_20200803_1951'),
    ]

    operations = [
        migrations.AlterField(
            model_name='therapy',
            name='stopien_sprawnosci',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=1), null=True, size=None),
        ),
    ]
