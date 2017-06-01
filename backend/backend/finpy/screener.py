"""
from django.conf import settings
settings.configure()
import models
"""
#from django.conf import settings
#settings.configure()

#import backtester
#settings.configure(default_settings=backtester, DEBUG=True)

from models import Stock

stocks = Stock.objects.all()

for stock in stocks:
    print stock.name

print "TEST"
