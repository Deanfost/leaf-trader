from finpy.models import Stock
import cPickle as pickle
import random

stocks = Stock.objects.all()

sector_dict = pickle.load(open("sectorsave.p", "rb"))

def undervalued():
    undervalued_list = []
    for stock in stocks :
        if stock.PE_ratio <= 1.0 and stock.PBook_ratio  <= 1.2:
            undervalued_list.append(stock)

    return undervalued_list


def undervalued_growth():
    undervalued_growth_list = []
    for stock in stocks:
        if stock.PE_ratio <= 5.0 and stock.PEG_ratio <=2.0:
            undervalued_growth_list.append(stock)

    return undervalued_growth_list

def high_growth():
    high_growth_list = []
    for stock in stocks:
        if stock.revenueGrowth >= 25.0:
            high_growth_list.append(stock)

    return high_growth_list


def low_volatility():
    low_volatility_list = []
    for stock in stocks:
        if stock.beta < 1.15 :
            low_volatility_list.append(stock)
    return low_volatility_list

    #//////////////////////////// sector specific presets


def siliconValley():
    siliconValley_list = []
    lister = sector_dict["Technology"]
    starter_list = []
    intermediate_list = []

    for tic in lister:
        starter_list.append(Stocks.objects.get(ticker = tic ))

    for stock in starter_list:
        if stock.current_ratio > 1.1 and stock.profit_margin > 18.0: # where 18 is the sector average
            intermediate_list.append(stock)
            intermediate_list = random.shuffle(intermediate_list)

    if len(intermediate_list) >= 15:
        for i in range(15):
            siliconValley.append(intermediate_list[i])

    else:
        for i in range(len(intermediate_list)):
            siliconValley.append(intermediate_list[i])

    return siliconValley_list

def manufacturing():
    manufacturing_list = []
    lister = sector_dict["Industrials"]
    starter_list = []
    intermediate_list = []

    for tic in lister:
        starter_list.append(Stocks.objects.get(ticker = tic ))

    for stock in starter_list:
        if stock.return_on_assets > 5.0 and stock.profit_margin > 18.0: # where 18 is the sector average
            intermediate_list.append(stock)
            intermediate_list = random.shuffle(intermediate_list)

    if len(intermediate_list) >= 15:
        for i in range(15):
            manufacturing_list.append(intermediate_list[i])

    else:
        for i in range(len(intermediate_list)):
            manufacturing_list.append(intermediate_list[i])

    return manufacturing_list

def healthCare():
    healthcare_list = []
    lister = sector_dict["Health Care"]
    starter_list = []
    intermediate_list = []

    for tic in lister:
        starter_list.append(Stocks.objects.get(ticker = tic ))

    for stock in starter_list:
        free_cash_yield = stock.cashflow / stock.market_cap # comparable to pe ratio but more oriented around cash flow which is more important for health care industry


        if stock.return_on_assets > 6.0 and free_cash_yield > 6.0: # where 5.5 is the sector average
            intermediate_list.append(stock)
            intermediate_list = random.shuffle(intermediate_list)

    if len(intermediate_list) >= 15:
        for i in range(15):
            healthcare_list.append(intermediate_list[i])

    else:
        for i in range(len(intermediate_list)):
            healthcare_list.append(intermediate_list[i])

    return healthcare_list


def finance():
    finance_list = []
    lister = sector_dict["Financials"]
    starter_list = []
    intermediate_list = []

    for tic in lister:
        starter_list.append(Stocks.objects.get(ticker = tic ))

    for stock in starter_list:
        if stock.return_on_assets > 6.0 and stock.profit_margin > 20.0: # where 17 is the industry standard
            intermediate_list.append(stock)
            intermediate_list = random.shuffle(intermediate_list)

    if len(intermediate_list) >= 15:
        for i in range(15):
            finance_list.append(intermediate_list[i])

    else:
        for i in range(len(intermediate_list)):
            finance_list.append(intermediate_list[i])

    return finance_list

def energy():
    energy_list = []
    lister = sector_dict["Energy"]
    starter_list = []
    intermediate_list = []

    for tic in lister:
        starter_list.append(Stocks.objects.get(ticker = tic ))

    for stock in starter_list:
        if stock.debt_equity_ratio < 115.0 and stock.profit_margin > 20.0: # where 17 is the industry standard
            intermediate_list.append(stock)
            intermediate_list = random.shuffle(intermediate_list)

    if len(intermediate_list) >= 15:
        for i in range(15):
            energy_list.append(intermediate_list[i])

    else:
        for i in range(len(intermediate_list)):
            energy_list.append(intermediate_list[i])

    return energy_list
