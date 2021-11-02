
from tvDatafeed import TvDatafeed, Interval
import datetime
import pandas as pd
from Configuration_StOb import *


def get_data_from_TV(exchange_symbols_dict, interval, bars):
    '''Function to get historical data from TradingView.
    Function expects a dictionary with symbols, interval and bars.'''
    data_frame_from_TV = TvDatafeed(auto_login = False, chromedriver_path = '/usr/bin/chromedriver')
    # Dictionary for storing stock data per exchange
    data_frame_dict = {}
    data_frame_list = []
    for key in exchange_symbols_dict.keys():
        for i in range(len(exchange_symbols_dict[key])):
            symb_hist = data_frame_from_TV.get_hist(symbol = exchange_symbols_dict[key][i], exchange = key, interval = interval, n_bars = bars)
            symb_hist_close = symb_hist[['close']]
            symb_hist_renamed = symb_hist_close.rename(columns = {'close' : exchange_symbols_dict[key][i]})
            data_frame_list.append(symb_hist_renamed)
            if(i==len(exchange_symbols_dict[key])-1):
                data_frame = pd.concat(data_frame_list, axis = 1)
                data_frame_dict[key] = data_frame
                data_frame_list = []
                data_frame = pd.DataFrame()
    return data_frame_dict