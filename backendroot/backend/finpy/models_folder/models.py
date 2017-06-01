from __future__ import unicode_literals
from django.conf import settings
settings.configure()
from django.db import models

class Stock(models.Model):
    ticker = models.CharField(max_length = 10)
    name = models.CharField(max_length = 128)
    last_price = models.IntegerField(default = 0)
    market_cap = models.CharField(max_length = 20)
    sector = models.CharField(max_length = 128)

    class Meta :
        app_label = "finpy"

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.ticker


class test(models.Model):
    name = models.CharField(max_length = 128)



    # install class Meta if you want some additional ordering of the instances
