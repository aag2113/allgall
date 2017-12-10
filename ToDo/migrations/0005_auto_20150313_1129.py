# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ToDo', '0004_task_sortorder'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='task',
            options={'ordering': ['sortOrder', 'status', 'created_date']},
        ),
    ]
