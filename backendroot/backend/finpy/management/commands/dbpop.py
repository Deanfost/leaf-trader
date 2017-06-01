
import csv
from django.core.management.base import BaseCommand
from finpy.models import Stock




class Command(BaseCommand):
    def handle(self, *args, **options):
        with open("/Users/rishubnahar/Desktop/djangoprojects/marketmaster/backend/finpy/fixedoutput.csv", "rU") as csvfile:
            reader = csv.reader(csvfile)
            print "test1"
            for line in reader:
                try:
                    # stock = Stock(ticker = line[0], name = line[1], last_price = float(line[2]), sector = line[5], market_cap = line[3])
                    # stock.save()
                    print "testing"
                except:
                    continue
                    print "SKIPPING "  + str(line[1])
                #print line

        #print "test"
