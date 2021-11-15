from tvDatafeed import TvDatafeed, Interval
import datetime
import pandas as pd
from CalcVal import *
from Configuration_StOb import *
from GetData import *


dict_test = get_data_from_TV(exch_symbs, Interval.in_daily, 500)
x = calc_rolling_mean(dict_test, rolling_window, 1)
z = calc_comp(x, first_comp, second_comp, third_comp)

for key in z.keys():
	print(key)
	print(type(z[key]))
