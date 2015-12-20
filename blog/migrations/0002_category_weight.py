# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='weight',
            field=models.IntegerField(default=1, verbose_name='weight'),
            preserve_default=False,
        ),
    ]
