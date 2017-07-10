from googlefinance import getQuotes



with open("s&P500.csv", "r") as spfile:
    for line in spfile:
        stock_line = line.split(",")

        Ticker = stock_line[0]
        print (getQuotes(str(Ticker)))
