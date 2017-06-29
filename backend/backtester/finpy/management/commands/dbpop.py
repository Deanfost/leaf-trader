
import csv
from django.core.management.base import BaseCommand
from finpy.models import Stock
from finpy.models import test




class Command(BaseCommand):
    def handle(self, *args, **options):
        with open("/Users/rishubnahar/Desktop/djangoprojects/paper-trader/backend/backend/finpy/s&P500.csv", "rU") as csvfile:
            reader = csv.reader(csvfile)


            for line in reader:
                #print line[0]
                try:
                     print "test3"
                     test =  Test(name = "test")
                     test.save()
                     #print line
                #     stock = Stock.objects.create(ticker = line[0], name = line[1], PBook_ratio = float(line[13]), Dividend_Yield = float(line[4]), Book_Value = float(line[7]), PE_ratio = float(line[5]), market_cap = float(line[10]), last_price = float(line[3]), sector = line[2], PS_ratio = float(line[12]), EPS_ratio  = float(line[6]))
                    # stock = Stock.objects.create(name = "AAPL")
                    # print stock.name
                    # stock.save()

                     print "testing"

                except:
                    continue
                    print "SKIPPING "  + str(line[1])
                #print line

        #print "test"
