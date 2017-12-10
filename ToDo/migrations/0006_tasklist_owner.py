# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ToDo', '0005_auto_20150313_1129'),
    ]

    operations = [
        migrations.AddField(
            model_name='tasklist',
            name='owner',
            field=models.ForeignKey(default=1, to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE),
            preserve_default=False,
        ),
    ]
