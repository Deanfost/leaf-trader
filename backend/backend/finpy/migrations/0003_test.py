# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('finpy', '0002_auto_20170527_1720'),
    ]

    operations = [
        migrations.CreateModel(
            name='test',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=128)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
