# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('ToDo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='completed_date',
            field=models.DateTimeField(default=datetime.datetime(1, 1, 1, 0, 0), verbose_name=b'Date Completed'),
            preserve_default=True,
        ),
    ]
