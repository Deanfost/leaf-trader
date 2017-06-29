from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from jsonfield import JSONField
from django.db.models.signals import post_save
from django.dispatch import receiver
from datetime import datetime



class Stock(models.Model):
    ticker = models.CharField(max_length = 10)
    name = models.CharField(max_length = 128)
    last_price = models.FloatField(default = 0.0)
    market_cap = models.CharField(max_length = 20)
    sector = models.CharField(max_length = 128)
    PE_ratio = models.FloatField(default = 0.0)
    EPS_ratio = models.FloatField(default = 0.0)
    PS_ratio = models.FloatField(default = 0.0)
    PBook_ratio = models.FloatField(default = 0.0)
    Dividend_Yield = models.FloatField(default = 0.0) # we can get rid of this
    Book_Value  = models.FloatField(default = 0.0) # also get rid of this
    last_price_refresh = models.DateTimeField(default=datetime.now) # notice we are not putting datetime.now() with paranthesis. Plan on updating this every week
    last_ratio_refresh = models.DateTimeField(default = datetime.now) # Plan on updating the ratios every month



    id = models.BigIntegerField(primary_key=True)
    class Meta :
        app_label = "finpy"

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.ticker

class test(models.Model):
    name = models.CharField(max_length = 10 )

    def __str__(self):
        return self.name


class UserProfile(models.Model):
    email = models.CharField(max_length = 100)
    username = models.CharField(max_length = 50)
    #bio = models.TextField(max_length=500, blank=True)
    networth = models.IntegerField(default = 15000,)
    cash = models.IntegerField(default = 15000)
    holdingsdict = JSONField(default = dict)
    created = models.DateTimeField(default=datetime.now) # notice we are not putting datetime.now() with paranthesis. Plan on updating this every week


    def __str__(self):
        return self.username

class savedScreener(models.Model): # these belong to a specific user profile
    name = models.CharField(max_length = 100)
    user = models.ForeignKey(UserProfile)
    sectors = models.CharField(max_length = 200) # later on we are going to have to split this string into a list
    lower_limit = models.IntegerField(default = 0)
    upper_limit = models.IntegerField(default = None)
    ratios = JSONField(default = dict)


    def __str__(self):
        return self.name
"""


class Screener(models.Model):
    name = models.TextField(max_length = 500, blank = True)
    date_lastused = models.
"""
# class test(models.Model):
#     name = models.CharField(max_length = 128)



    # install class Meta if you want some additional ordering of the instances
