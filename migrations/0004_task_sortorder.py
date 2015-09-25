# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ToDo', '0003_tasklist_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='sortOrder',
            field=models.IntegerField(default=2147483647),
            preserve_default=True,
        ),
    ]
