
import json
from config import property_loader
from processor.helper import *
import pandas as pd



# PROCESSORS
def current_value():
    stock_list = property_loader.load_config()
    for stock in stock_list:
        current_price = get_current_price(stock)
        print(stock + ' : ' + str(current_price))

def info():
    print('info')
    # msft = yf.Ticker("MSFT")
    # print('hello')
    # json_out = json.dumps(msft.info, indent=4)
    # print(json_out)
    # data = yf.download("SPY AAPL", start="2017-01-01", end="2017-04-30")

def history():
    stock_list = property_loader.load_config()
    for stock in stock_list:
        hist =  get_history(stock, '5d' , '1h')
        print(stock + ' : ' )
        print(hist.to_string())


def buy_and_sell_same_day():
    stock_list = property_loader.load_config()
    for stock in stock_list:
        diff_df = get_open_close_diff(stock, '5d' , '1d')
        print(diff_df)
