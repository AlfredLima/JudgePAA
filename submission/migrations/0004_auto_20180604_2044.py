# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('submission', '0003_auto_20180604_1942'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submission',
            name='evaluation',
            field=models.CharField(max_length=200, default='Avaliando'),
        ),
        migrations.AlterField(
            model_name='submission',
            name='file',
            field=models.FileField(upload_to=''),
        ),
    ]
