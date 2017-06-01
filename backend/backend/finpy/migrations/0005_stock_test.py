# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('finpy', '0004_auto_20170527_1738'),
    ]

    operations = [
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ticker', models.CharField(max_length=10)),
                ('name', models.CharField(max_length=128)),
                ('last_price', models.IntegerField(default=0)),
                ('market_cap', models.IntegerField(default=0)),
                ('sector', models.CharField(max_length=128)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
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
