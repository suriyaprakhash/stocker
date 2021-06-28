
import json
from config import property_loader
from processor.helper import *
import pandas as pd
from processor.model import learn, predict



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

def history(no_of_days, interval):
    stock_list = property_loader.load_config()
    for stock in stock_list:
        hist =  get_history(stock, no_of_days , interval)
        print(stock + ' : ' )
        print(hist.to_string())
        return hist


def fit():
    open_price_list = []
    close_price_list = []
    hist_df = history('5d', '1d')
    train_hist_df = hist_df.head(len(hist_df) - 1)
    for ind in train_hist_df.index:
        # day_list.append(hist_df['Date'][ind])
        open_price_list.append([train_hist_df['Close'][ind]])
        close_price_list.append(train_hist_df['Close'][ind])
    print(open_price_list)
    print(close_price_list)
    learn(open_price_list, close_price_list)
    print(predict([[270]]))


def buy_and_sell_same_day():
    stock_list = property_loader.load_config()
    for stock in stock_list:
        diff_df = get_open_close_diff(stock, '10{TypeError}tuple indices must be integers or slices, not strd' , '1d')
        print(diff_df)
