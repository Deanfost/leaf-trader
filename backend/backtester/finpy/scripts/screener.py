"""
from django.conf import settings
settings.configure()
import models
"""
#from django.conf import settings
#settings.configure()

#import backtester
#settings.configure(default_settings=backtester, DEBUG=True)

from finpy.models import Stock
from googlefinance import getQuotes
import urllib2
from bs4 import BeautifulSoup
from bs4 import SoupStrainer
import re
from collections import defaultdict
from googlefinance import getQuotes
import datetime
from django.utils import timezone
#from datetime import timezone


print "test"

# what you want to make sure is that the sector list is passed as a string, then we will use split to convert it to a proper list
#sector_list, ratio_list, price_range, marketcap should be the different types of args available in *args

def soup(ticker):
    vardict= defaultdict(int)
    url = "https://finance.yahoo.com/quote/" + ticker + "/key-statistics?p=" + ticker
    content = urllib2.urlopen(url).read()
    only_span = SoupStrainer(["span", "td"])
    data = BeautifulSoup(content, "lxml", parse_only= only_span) # this is creating a BeautifulSoup object that we can enact BeautifulSoup methods on

    #print data.get_text()
    #find_string = data.get_text().find_all(text=re.compile('Trailing P/E'), limit=1)

    var = data.find(text = "Trailing P/E").findNext("td")
    var2 = data.find(text = "Price/Book").findNext("td")
    var3 = data.find(text = "Price/Sales").findNext("td")
    var4 = data.find(text = "Diluted EPS").findNext("td")

    print var.text + "Soup"
    print var2.text


    vardict["Price_Earnings"] = var.text
    vardict["Price_Book"] = var2.text
    vardict["Price_Sales"] = var3.text
    vardict["Diluted_EPS"] = var4.text


    return vardict



def screenerfunction(kwargs):

    stocks = Stock.objects.all()

    screened_sector_list = []
    screened_cap_list = []
    screened_price_list = []
    screened_ratio_list = []
    joint_list = []



    full_list = [screened_sector_list, screened_cap_list, screened_price_list]
    new_full_list = []

    current_time = timezone.now()

###### ratios are going to have to be passed in dict format

    for key in kwargs:
        if key == "sector_list":
            sector_list = kwargs[key]
        else:
            sector_list = None
        if key == "ratio_dict":
            ratio_dict = kwargs[key]
        else:
            ratio_dict = None
        if key == "marketcap":
            marketcap = kwargs[key]
        else:
            marketcap = "Mega" #default should be none in real life
        if key == "price_range":
            price_range == kwargs[key] # price must be passed as list
        else:
            price_range = [100.0,200.0]
            # price range will probably be a tuple value
        if key == "ratio_dict":
            ratio_dict == kwargs[key]
        else:
            ratio_dict = {"PE_ratio" : 17}


    if sector_list is not None:
        for stock in stocks:
            for sector in sector_list:
                if stock.sector == sector:
                    screened_sector_list.append(stock)

        # ratio_dict would have to be created in views such that there are no blanks can only be the ratios that the user inputs
        #ratio_list = soup(stock.ticker) # using BeautifulSoup to scrape the ratio values from yahoo finance
        #if ratio_dict is not None:
        #    for ratiokey in ratio_dict:
        #        if ratio_dict[ratiokey] == vardict[ratiokey]:
        #            screened_list.append(stock)
        #        else:
        #            if stock in screened_list:
        #                screened_list = screened_list.remove(stock)

    if marketcap is not None:

        if (len(sector_list) > 0 ):
            for stock in screened_sector_list:

                if (stock.market_cap > 200):
                    stockcap = "Mega"
                if(stock.market_cap < 200 and stock.market_cap > 10):
                    stockcap = "Large"
                if(stock.market_cap < 10 and stock.market_cap > 2):
                    stockcap = "Mid"
                if(stock.market_cap < 2):
                    stockcap = "Small"

                if(stockcap == marketcap):
                    screened_cap_list.append(stock)

        else: # if there is no sector specified
            for stock in stocks:
                if (stock.market_cap > 200):
                    stockcap = "Mega"
                if(stock.market_cap < 200 and stock.market_cap > 10):
                    stockcap = "Large"
                if(stock.market_cap < 10 and stock.market_cap > 2):
                    stockcap = "Mid"
                if(stock.market_cap < 2):
                    stockcap = "Small"


                if stockcap == marketcap:
                    screened_cap_list.append(stock)



    if price_range is not None: # price filter
        lower_limit = price_range[0]
        upper_limit = float(price_range[1])

        if(len(screened_sector_list) > 0 and len(screened_cap_list) > 0):
            joint_list = list(set(screened_sector_list).intersection(screened_cap_list))
            print "FIRST OPTION FOR PRICE"

            if(len(joint_list) == 0 ):
                return joint_list
                # end of script, there are no matches
            else:
                for stock in joint_list:
                    time_delta = current_time - stock.last_price_refresh

                    if(time_delta.total_seconds()  < 604800) :  # of seconds in a week
                        if(stock.last_price <= upper_limit and stock.last_price >= lower_limit) :
                            screened_price_list.append(stock)
                    else:
                        ticker  = stock.ticker
                        current_price = getQuotes(str(ticker))
                        print current_price
                        print "THIS IS THE TICKER TO ANALYZE " + str(stock.ticker)
                        print "Making this api call to get the modern price"
                        current_price = float(current_price[0]["LastTradePrice"])

                        stock.last_price_refresh = datetime.datetime.now()
                        stock.last_price = current_price
                        stock.save()
                        # updating the stocks price since it hasnt been refreshed for a whole week
                        if(stock.last_price <= upper_limit and stock.last_price >= lower_limit) :
                            screened_price_list.append(stock)

        elif(len(screened_sector_list) > 0 and len(screened_cap_list) == 0) : # there is only a sector attribute
            for stock in screened_sector_list:
                time_delta = current_time - stock.last_price_refresh

                if(time_delta.total_seconds()  < 604,800) :  # of seconds in a week
                    if(stock.last_price <= upper_limit and stock.last_price >= lower_limit) :
                        screened_price_list.append(stock)
                else:
                    ticker  = stock.ticker
                    current_price = getQuotes(str(ticker))
                    current_price = float(current_price[0]["LastTradePrice"])
                    stock.last_price_refresh = datetime.datetime.now()
                    stock.last_price = current_price
                    stock.save()
                    # updating the stocks price since it hasnt been refreshed for a whole week
                    if(stock.last_price <= upper_limit and stock.last_price >= lower_limit) :
                        screened_price_list.append(stock)

        elif(len(screened_cap_list) > 0 and len(screened_sector_list) == 0 ): # there is only market_cap
            for stock in screened_cap_list:
                time_delta = current_time - stock.last_price_refresh

                if(time_delta.total_seconds()  < 604,800) :  # of seconds in a week
                    if(stock.last_price <= upper_limit and stock.last_price >= lower_limit) :
                        screened_price_list.append(stock)
                else:
                    ticker  = stock.ticker
                    current_price = getQuotes(str(ticker))
                    current_price = float(current_price[0]["LastTradePrice"])
                    stock.last_price_refresh = datetime.datetime.now()
                    stock.last_price = current_price
                    stock.save()
                    # updating the stocks price since it hasnt been refreshed for a whole week
                    if(stock.last_price <= upper_limit and stock.last_price >= lower_limit) :
                        screened_price_list.append(stock)
        else: # there are no sector or market cap attributes
            for stock in stocks:
                time_delta = current_time - stock.last_price_refresh

                if(time_delta.total_seconds()  < 604,800) :  # of seconds in a week
                    if(stock.last_price <= upper_limit and stock.last_price >= lower_limit) :
                        screened_price_list.append(stock)
                else:
                    ticker  = stock.ticker
                    current_price = getQuotes(str(ticker))
                    current_price = float(current_price[0]["LastTradePrice"])
                    stock.last_price_refresh = datetime.datetime.now()
                    stock.last_price = current_price
                    stock.save()
                    # updating the stocks price since it hasnt been refreshed for a whole week
                    if(stock.last_price <= upper_limit and stock.last_price >= lower_limit) :
                        screened_price_list.append(stock)



    for lister in full_list:
        if len(lister) > 0 :
            new_full_list.append(lister)  # this is a list of all the list that have been filled with arguments by the user

    finalresult = set(new_full_list[0])
    for lister in new_full_list[1:]:
        finalresult.intersection_update(lister)   #  this is a list that has the stocks common to all the lists populated by the user

    print "********* INTERMEDIATE FINAL RESULT ************"
    print finalresult

    if ratio_dict is not None:

        if(len(finalresult) > 0 ) :
            for stock in finalresult:
                ratio_continue = True
                time_ratio_delta = current_time - stock.last_ratio_refresh
                if (time_ratio_delta.total_seconds() > 2678400) :

                    print "MAKING THIS SOUP CALL"

                    updated_ratio_dict = soup(stock.ticker)
                    print "********* SOUP DICT ************"
                    print updated_ratio_dict
                    print updated_ratio_dict["Price_Earnings"]
                    #print updated_ratio_dict["PE_Ratio"]
                    #stocker = Stock.objects.get(ticker = stock.ticker)
                    stock.PBook_ratio = float(str(updated_ratio_dict["Price_Book"]))
                    stock.PS_ratio = float(str(updated_ratio_dict["Price_Sales"]))
                    stock.EPS_ratio = float(str(updated_ratio_dict["Diluted_EPS"]))
                    stock.PE_ratio = float(str(updated_ratio_dict["Price_Earnings"]))
                    stock.last_ratio_refresh = datetime.datetime.now()
                    stock.save()

                for ratio in ratio_dict:
                    if ratio == "PE_ratio" :
                        if(abs(stock.PE_ratio - ratio_dict["PE_ratio"]) < 2 ) :
                            continue
                        else:
                            ratio_continue = False
                    if ratio == "PS_ratio":
                        if (abs(stock.PS_ratio - ratio_dict["Price_sales"]) < 2 ):
                            continue
                        else:
                            ratio_continue = False

                    if ratio == "PBook_ratio":
                        if (abs(stock.PBook_ratio - ratio_dict["Price_Book"]) < 2 ):
                            continue
                        else:
                            ratio_continue = False
                    if ratio == "EPS_ratio":
                        if (abs(stock.EPS_ratio - ratio_dict["Diluted_EPS"]) < 2 ):
                            continue
                        else:
                            ratio_continue = False

                if (ratio_continue == True):
                    screened_ratio_list.append(stock)

        else: # there was no other parameter
            for stock in stocks:
                ratio_continue = True
                time_ratio_delta = current_time - stock.last_ratio_refresh
                if (time_ratio_delta.total_seconds() > 2678400) :

                    updated_ratio_dict = soup(stock.ticker)
                    #stocker = Stock.objects.get(ticker = stock.ticker)
                    stock.PBook_ratio = updated_ratio_dict["Price_Book"]
                    stock.PS_ratio = updated_ratio_dict["Price_Sales"]
                    stock.EPS_ratio = updated_ratio_dict["Diluted_EPS"]
                    stock.PE_ratio = updated_ratio_dict["PE_ratio"]
                    stock.last_ratio_refresh = datetime.datetime.now()
                    stock.save()

                for ratio in ratio_dict:
                    if ratio == "PE_ratio" :
                        if(abs(stock.PE_ratio - ratio_dict["PE_ratio"]) < 2 ) :
                            continue
                        else:
                            ratio_continue = False
                    if ratio == "PS_ratio":
                        if (abs(stock.PS_ratio - ratio_dict["Price_Sales"]) < 2 ):
                            continue
                        else:
                            ratio_continue = False

                    if ratio == "PBook_ratio":
                        if (abs(stock.PBook_ratio - ratio_dict["Price_Book"]) < 2 ):
                            continue
                        else:
                            ratio_continue = False
                    if ratio == "EPS_ratio":
                        if (abs(stock.EPS_ratio - ratio_dict["Diluted_EPS"]) < 2 ):
                            continue
                        else:
                            ratio_continue = False

                if (ratio_continue == True):
                    screened_ratio_list.append(stock)


    full_list = [screened_sector_list, screened_cap_list, screened_price_list, screened_ratio_list]

    new_full_list = []
    for lister in full_list:
        if len(lister) > 0 :
            new_full_list.append(lister)

    finalresult = set(new_full_list[0])
    for lister in new_full_list[1:]:
        finalresult.intersection_update(lister)


    print  "**************************************************"

    #print list(finalresult)

    print  "**************************************************"
    print screened_sector_list
    print  "**************************************************"
    print screened_price_list
    print  "**************************************************"
    print screened_cap_list
    print  "**************************************************"
    print screened_ratio_list






    return list(finalresult)



if __name__ == "__main__":
    list = ["AAPL", "GOOG", "MSFT", "TSLA","FB", "TWTR", "GS"]

    for item in list:
        soup(item)
    print "FINISHED"
