from tvDatafeed import TvDatafeed, Interval
import datetime
import pandas as pd
from Configuration_StOb import *
from GetData import *



def calc_rolling_mean(exchange_symbols_dict, rolling_window, minimum_periods):
	'''Function to calculate rolling mean values for symbols ginve in the dictionary.'''
	exchange_symbols_dict_mean = {}
	exchange_symbols_dict_mean_reverse = {}
	for key in exchange_symbols_dict.keys():
		exchange_symbols_dict_mean[key] = exchange_symbols_dict[key].rolling(window = rolling_window, min_periods=minimum_periods).mean()
		# Reverse the order, so that latest values are on top
		exchange_symbols_dict_mean_reverse[key] = exchange_symbols_dict_mean[key][::-1]
	return exchange_symbols_dict_mean_reverse

def calc_comp(exchange_symbols_dict_mean, short_time, medium_time, long_time):
	dict_calc_vals = {}
	exchange_symbols_dict_calc_vals = {}
	list_calc_vals = []
	for key in exchange_symbols_dict_mean.keys():
		for symb in list(exchange_symbols_dict_mean[key].columns):
			list_calc_vals.append(((exchange_symbols_dict_mean[key][symb].iloc[0]-exchange_symbols_dict_mean[key][symb].iloc[short_time])/exchange_symbols_dict_mean[key][symb].iloc[short_time])*100)
			list_calc_vals.append(((exchange_symbols_dict_mean[key][symb].iloc[0]-exchange_symbols_dict_mean[key][symb].iloc[medium_time])/exchange_symbols_dict_mean[key][symb].iloc[medium_time])*100)
			list_calc_vals.append(((exchange_symbols_dict_mean[key][symb].iloc[0]-exchange_symbols_dict_mean[key][symb].iloc[long_time])/exchange_symbols_dict_mean[key][symb].iloc[long_time])*100)
			dict_calc_vals[symb] = list_calc_vals
			list_calc_vals = []
		exchange_symbols_dict_calc_vals[key] = pd.DataFrame.from_dict(dict_calc_vals)
		dict_calc_vals = {}
	return exchange_symbols_dict_calc_vals