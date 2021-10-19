

from tvDatafeed import TvDatafeed, Interval
import datetime
import numpy as np
import pandas as pd
from Configuration_StOb import *

tdf = TvDatafeed(auto_login = False, chromedriver_path = '/usr/bin/chromedriver')

def get_data(exchange_symbols, interval, bars):
    data_frame = []
    for key in exchange_symbols.keys():
        print(key)
        for i in range(len(exchange_symbols[key])):
            hist = tdf.get_hist(symbol = exchange_symbols[key][i], exchange = key, interval = interval, n_bars = bars)
            hist_reverse = hist[::-1]
            hist_close = hist_reverse[['close']]
            hist_renamed = hist_close.rename(columns = {'close' : exchange_symbols[key][i]})
            #hist_final = pd.concat()
            data_frame.append(hist_renamed)
            #print(data_frame.shape)
            #print(hist_renamed.head(10))
            #print(type(hist))
    hist_final = pd.concat(data_frame, axis = 1)
    #print(hist_final.head())


get_data(exch_symbs, Interval.in_daily, 10)
#tdf_1 = tdf.get_hist(symbol = "ADS", exchange = "XETR", interval = Interval.in_daily, n_bars = 5000)
##print(tdf_1.head())
##print(tdf_1.index)
#tdf_1_close = tdf_1_close[::-1]
#tdf_1_close.rename(columns={'close' : 'ADS'}, inplace = True)
#print(tdf_1_close.head())
#print(list(tdf_1_close.columns))
#tdf_2 = tdf.get_hist(symbol = "AIR", exchange = "XETR", interval = Interval.in_daily, n_bars = 5000)
#tdf_2_close = tdf_2[['close']]
#tdf_2_close = tdf_2_close[::-1]
#tdf_2_close.rename(columns = {'close' : 'AIR'}, inplace = True)
#print(list(tdf_2_close.columns))#

#a = pd.concat([tdf_1_close, tdf_2_close], axis = 1)

#print(a.head())
