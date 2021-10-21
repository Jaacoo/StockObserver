
from tvDatafeed import TvDatafeed, Interval
import datetime
import pandas as pd
from Configuration_StOb import *


def get_data(exchange_symbols, interval, bars):
    tdf = TvDatafeed(auto_login = False, chromedriver_path = '/usr/bin/chromedriver')
    data_frame_dict = {}
    data_frame_list = []
    for key in exchange_symbols.keys():
        print(key)
        for i in range(len(exchange_symbols[key])):
            print(exchange_symbols[key][i])
            hist = tdf.get_hist(symbol = exchange_symbols[key][i], exchange = key, interval = interval, n_bars = bars)
            hist_close = hist[['close']]
            hist_renamed = hist_close.rename(columns = {'close' : exchange_symbols[key][i]})
            data_frame_list.append(hist_renamed)
            if(i==len(exchange_symbols[key])-1):
                data_frame = pd.concat(data_frame_list, axis = 1)
                data_frame_dict[key] = data_frame
                data_frame_list = []
                data_frame = pd.DataFrame()
    return data_frame_dict

