# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('full_name', models.CharField(max_length=200)),
                ('phone_number', models.CharField(blank=True, max_length=15, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')])),
                ('company', models.CharField(max_length=200)),
                ('department', models.CharField(max_length=200)),
                ('occupation', models.CharField(max_length=200)),
            ],
        ),
    ]
