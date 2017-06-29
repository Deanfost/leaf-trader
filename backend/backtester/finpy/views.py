from django.shortcuts import render, redirect
from django.http import HttpResponse
#from portfolio_constructor import get_adjusted_close
#from finpy.screener import match_params
from collections import defaultdict
import os
import csv
from finpy.models import Stock, test, UserProfile
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from scripts.screener import soup, screenerfunction
from googlefinance import getQuotes
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.contrib.auth import authenticate, login, logout

#from scripts.simulate import newtotals

#python manage.py runserver --settings=backtester.settings
ticker_list = []
# Create your views here.

#x = lister2.delay(None, None, None)


def signup(request):
    print "RENDERING"
    if request.method == "POST":
        print "HEY THERE"
        username = request.POST.get("username")
        #email = request.POST.get("email")
        #password = request.POST.get("password")
        print username
        #print email
        #user = User.objects.create_user(username, email, password)
        #user.save()

        #prof = UserProfile(email, username)
        #prof.save()

        return redirect("landing_page")

    response  = render(request, "finpy/signup.html")
    return response





def practiceAjax(request):
    print "CALLING AJAX"
    data = {"message" : "AJax call"}
    return data

def validate_username(request):
    print "SENDING THIS AJAX CALL"
    username = request.GET.get('username', None) # where none acts as the default value of username if none is passed
    data = {
        'is_taken': User.objects.filter(username__iexact=username).exists()
    }
    return JsonResponse(data)

def practiceAjax(request):
    username = request.GET.get("username", None)
    data = {
        "name" : str(username + "AJAX")
    }
    return JsonResponse(data)


def socialogin(request):

   if request.user.is_authenticated() :
       print "AUTHENICATED"



       obj=  request.user
       print obj.email
       print obj.username

       profiles = UserProfile.objects.all()
       print profiles



       try :
           chosenOne = UserProfile.objects.get(email = obj.email)
       except:
            chosenOne = None

       print "THE CHOSEN ONE"
       print chosenOne

       if (chosenOne is None):
           newProfile = UserProfile( email = obj.email, username = obj.username, cash = 15000, networth = 15000)
           newProfile.save()
           return redirect("landing_page")


       else:
            return redirect("landing_page")


   else : # get request
        print "NOT AUTHENICATED"
        return render_to_response('finpy/social_login.html')


def loggingIn(request):

    if request.method == "POST" :
        users = User.objects.all()
        print users
        chosenName = request.POST.get("username")
        password = request.POST.get("password")
        """
        try:
            chosenOne = User.objects.get(username = chosenName)
        except:
            chosenOne = None
        """

        chosenOne = authenticate(username = chosenName, password = password)

        print "THIS IS USER"
        print chosenOne

        if chosenOne is not None:
            login(request, chosenOne)
            return redirect("landing_page")
        else:
            notValid = True
            return render_to_response("finpy/login.html", {"notValid" : notValid})
    return render_to_response('finpy/login.html')



def altLogin(request):  # gooogle signin
    return render_to_response("finpy/google_signin.html")

def loggingout(request):
    logout(request)

    return redirect("landing_page")



def landing_page(request):
    print request.user
    print "That was the user object request for the second time "

    if (request.user.is_authenticated()):
        print "UUSER"
        print request.user.username
        response = render(request,"finpy/landing_page.html", {"user" : request.user})
    response = render(request,"finpy/landing_page.html")
    return response
    #stock = Stock.objects.all()

    print "************TASK STATE*************"
    #x = lister2.delay()
    #print x.request
    """
    #celery_task_result = AsyncResult(x.task_id)
    task_state = celery_task_result.state
    print task_state
    #print x.task_id
    #print str(lister2.AsyncResult(x.task_id).state)


    with open("/Users/rishubnahar/Desktop/djangoprojects/paper-trader/backend/backend/finpy/s&P500.csv", "rU") as csvfile:

        reader = csv.reader(csvfile)
        for line in reader :

            try :
                #stock = Stock(ticker = line[0], name = line[1], PBook_ratio = float(line[13]), Dividend_Yield = float(line[4]), Book_Value = float(line[7]), PE_ratio = float(line[5]), market_cap = float(line[10]), last_price = float(line[3]), sector = line[2], PS_ratio = float(line[12]), EPS_ratio  = float(line[6]))
                stock = Stock(ticker = "MSFT")
                stock.save()
            except:

                print "SKIPPING" + str(line[1])
                continue
    """
    #    i = 0

#        while i < 10:

        #    row = next(reader)

                 #print line
            #     stock = Stock.objects.create(ticker = line[0], name = line[1], PBook_ratio = float(line[13]), Dividend_Yield = float(line[4]), Book_Value = float(line[7]), PE_ratio = float(line[5]), market_cap = float(line[10]), last_price = float(line[3]), sector = line[2], PS_ratio = float(line[12]), EPS_ratio  = float(line[6]))
                # stock = Stock.objects.create(name = "AAPL")
                # print stock.name
                # stock.save()






    if request.method == "POST":
        stockquery = request.POST.get("stockquery")
        global ticker_list
        tickerlist.append(stockquery)
"""
    with open("/Users/rishubnahar/Desktop/djangoprojects/paper-trader/backend/backend/finpy/s&P500.csv", "rU") as csvfile:
        reader = csv.reader(csvfile)

        for line in reader :
            i = 0
            ticker = str(line[0])
            current_price = getQuotes("AAPL")

            current_price = float(current_price[0]["LastTradePrice"])
            print current_price
            break


            while(i<2):
                price = getQuotes(line[0])
                price = price[0]["LastTradePrice"]
                print price
                i+=1


"""

    #for s in stock:
    #    print s.name




def plotter(request):

    if request.method == "POST":
        startDate = request.POST.get("starting")
        endDate = request.POST.get("end")
        get_adjusted_close(ticker_list, startDate, endDate)

def screener(request) :


    ticker_list = []
    target_list = []

    # set every attribute to none as default
    sector_name =  [None,None,None,None,None]

    passed_dict = defaultdict(list)

    if request.method == "POST":

        #lister2.delay()
        #x = lister2.delay()

        print "************REQUESt***********"
    #    print x.task_id
    #    print x.backend

    #    print str(lister2.AsyncResult(x.task_id).state)


        #for i in range(100000000):
            #print i

        print "testing this POST"
        sector_name[0] = request.POST.get("Technology")
        sector_name[1] = request.POST.get("Health Care")
        sector_name[2] = request.POST.get("Finance")
        sector_name[3] = request.POST.get("Consumer Services")
        sector_name[4] = request.POST.get("Consumer Durables")
        #market_cap = request.POST.get("market_cap")


        #print "THIS IS MARKET CAP" + str(market_cap)

        for sector in sector_name:
            if sector is None:
                sector_name.remove(sector)


        passed_dict["sector_list"] = sector_name
        #passed_dict["marketcap"] = market_cap
        #target_list =  match_params("shortoutput.csv", passed_dict)
        screenerfunction(passed_dict)

        response  = render(request, "finpy/Frontend/html/screener.html", {"target_list" : target_list })
        return response

    response  = render(request, "finpy/Frontend/html/screener.html")
    return response






def screener2(request) :

    if request.method == "POST":
        sector = request.POST["sector"]

    target_list = []
    passed_dict = defaultdict(list)
    passed_dict["Sector"] == sector

    target_list =  match_params("shortoutput.csv", passed_dict)
    return HttpResponse("SUCCESS!")


def pdfDownload(request):
    path = ("finpy/s&P500.csv")
    filename = open(path, "r")
    response = HttpResponse(filename, content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="s&P500.csv"'

    return response







if __name__ == "__main__":
    print "HI"
