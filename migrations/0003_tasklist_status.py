# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ToDo', '0002_task_completed_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='tasklist',
            name='status',
            field=models.IntegerField(default=1),
            preserve_default=True,
        ),
    ]
