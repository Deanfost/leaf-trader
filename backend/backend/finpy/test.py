from googlefinance import getQuotes
import urllib2
from bs4 import BeautifulSoup
import re

"""
var = (getQuotes("AAPL"))[0]["LastTradeWithCurrency"]
print var
"""
def soup(ticker):
    url = "https://finance.yahoo.com/quote/" + ticker + "/key-statistics?p=" + ticker
    content = urllib2.urlopen(url).read()
    data = BeautifulSoup(content) # this is creating a BeautifulSoup object that we can enact BeautifulSoup methods on
    #print data.get_text()
    #find_string = data.get_text().find_all(text=re.compile('Trailing P/E'), limit=1)
    var = data.find(text = "Trailing P/E").findNext("td")
    var2 = data.find(text = "Price/Book").findNext("td")

    print var.text
    print var2.text
    
    return


if __name__ == "__main__":
    soup("AAPL")
