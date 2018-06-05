# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('submission', '0002_auto_20180603_2000'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='submission',
            name='password',
        ),
        migrations.AddField(
            model_name='submission',
            name='evaluation',
            field=models.CharField(default=b'Waiting', max_length=200),
        ),
        migrations.AddField(
            model_name='submission',
            name='grade',
            field=models.IntegerField(default=0),
        ),
    ]
