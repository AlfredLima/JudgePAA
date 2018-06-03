# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Submission',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('registration', models.CharField(max_length=8)),
                ('password', models.CharField(max_length=8)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('file', models.FileField(upload_to='')),
            ],
        ),
    ]
