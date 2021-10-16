

from tvDatafeed import TvDatafeed, Interval
import datetime
import numpy as np
import pandas as pd
from Configuration_StOb import *


tdf = TvDatafeed(auto_login = False, chromedriver_path = '/usr/bin/chromedriver')

hist = tdf.get_hist(symbol = 'MSFT', exchange = 'NASDAQ', interval = Interval.in_daily, n_bars = 1000)
hist_close = hist.close

print(hist.close)
