# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import __builtin__
import datetime
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('ticker', models.CharField(max_length=10)),
                ('name', models.CharField(max_length=128)),
                ('last_price', models.FloatField(default=0.0)),
                ('market_cap', models.CharField(max_length=20)),
                ('sector', models.CharField(max_length=128)),
                ('PE_ratio', models.FloatField(default=0.0)),
                ('EPS_ratio', models.FloatField(default=0.0)),
                ('PS_ratio', models.FloatField(default=0.0)),
                ('PBook_ratio', models.FloatField(default=0.0)),
                ('Dividend_Yield', models.FloatField(default=0.0)),
                ('Book_Value', models.FloatField(default=0.0)),
                ('last_price_refresh', models.DateTimeField(default=datetime.datetime.now)),
                ('last_ratio_refresh', models.DateTimeField(default=datetime.datetime.now)),
                ('id', models.BigIntegerField(serialize=False, primary_key=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='test',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=10)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('email', models.CharField(max_length=100)),
                ('username', models.CharField(max_length=50)),
                ('networth', models.IntegerField(default=15000)),
                ('cash', models.IntegerField(default=15000)),
                ('holdingsdict', jsonfield.fields.JSONField(default=__builtin__.dict)),
                ('created', models.DateTimeField(default=datetime.datetime.now)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
