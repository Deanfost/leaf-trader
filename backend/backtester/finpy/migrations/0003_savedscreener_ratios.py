# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import __builtin__
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('finpy', '0002_savedscreener'),
    ]

    operations = [
        migrations.AddField(
            model_name='savedscreener',
            name='ratios',
            field=jsonfield.fields.JSONField(default=__builtin__.dict),
            preserve_default=True,
        ),
    ]
