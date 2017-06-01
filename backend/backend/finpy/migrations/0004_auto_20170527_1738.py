# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('finpy', '0003_test'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Stock',
        ),
        migrations.DeleteModel(
            name='test',
        ),
    ]
