# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('finpy', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='savedScreener',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('sectors', models.CharField(max_length=200)),
                ('lower_limit', models.IntegerField(default=0)),
                ('upper_limit', models.IntegerField(default=None)),
                ('user', models.ForeignKey(to='finpy.UserProfile')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
