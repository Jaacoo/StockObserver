

from tvDatafeed import TvDatafeed, Interval
import datetime
import numpy as np
import pandas as pd
from Configuration_StOb import *

tdf = TvDatafeed(auto_login = False, chromedriver_path = '/usr/bin/chromedriver')

def get_data(symbols):
    for i in range(len(symbols)):
        hist = tdf.get_hist(symbol = symbols[i], exchange = "XETR", interval = Interval.in_daily, n_bars = 1000)
        hist_reverse = hist[::-1]
        print(hist_reverse.head())
        print(type(hist))

#hist = tdf.get_hist(symbol = "ADS", exchange = "XETR", interval = Interval.in_daily, n_bars = 1000)
get_data(dax_symbs)
#print(hist.head())
#print(hist.close)
