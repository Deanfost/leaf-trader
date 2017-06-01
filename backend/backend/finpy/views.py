from django.shortcuts import render
from django.http import HttpResponse
#from portfolio_constructor import get_adjusted_close
#from finpy.screener import match_params
from collections import defaultdict
import os
from finpy.models import Stock

#python manage.py runserver --settings=backtester.settings
ticker_list = []
# Create your views here.
def landing_page(request):
    response = render(request,"finpy/landing_page.html")
    stock = Stock.objects.all()

    for s in stock:
        print s.name

    return response


    if request.method == "POST":
        stockquery = request.POST.get("stockquery")
        global ticker_list
        tickerlist.append(stockquery)


def plotter(request):

    if request.method == "POST":
        startDate = request.POST.get("starting")
        endDate = request.POST.get("end")
        get_adjusted_close(ticker_list, startDate, endDate)

def screener(request) :


    ticker_list = []
    target_list = []

    # set every attribute to none as default
    sector_name =  None

    passed_dict = defaultdict(list)

    if request.method == "POST":
        print "test"
        sector_name = request.POST.get("selection")
        print sector_name

        if sector_name != None:
            passed_dict["Sector"].append(sector_name)
        target_list =  match_params("shortoutput.csv", passed_dict)

        response  = render(request, "finpy/Frontend/html/screener2.html", {"target_list" : target_list })
        return response

    response  = render(request, "finpy/Frontend/html/screener2.html")
    return response






def screener2(request) :

    if request.method == "POST":
        sector = request.POST["sector"]

    target_list = []
    passed_dict = defaultdict(list)
    passed_dict["Sector"] == sector

    target_list =  match_params("shortoutput.csv", passed_dict)
    return HttpResponse("SUCCESS!")


if __name__ == "__main__":
    print "HI"
