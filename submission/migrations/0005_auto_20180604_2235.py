# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('submission', '0004_auto_20180604_2044'),
    ]

    operations = [
        migrations.AddField(
            model_name='submission',
            name='email',
            field=models.EmailField(max_length=100, default='k@k.ufal.br'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='submission',
            name='name',
            field=models.CharField(max_length=100, default='Unnamed'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='submission',
            name='file',
            field=models.FileField(upload_to='codes/'),
        ),
    ]
