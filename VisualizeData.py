from tvDatafeed import TvDatafeed, Interval
import datetime
import pandas as pd
from CalcVal import *
from Configuration_StOb import *
from GetData import *
import matplotlib.pyplot as plt
import numpy as np


#def plot_raw_data():

data_test = get_data_from_TV(exch_symbs, Interval.in_daily,50)
x_raw = calc_rolling_mean(data_test, 1, 1)


#for key in x_raw.keys():
#	print(key)
#	print(x_raw[key].head())
#	x_raw[key].plot()

x_mean = calc_rolling_mean(data_test, rolling_window, 1)

#for key in x_mean.keys():
#	print(key)
#	print(x_mean[key].head())
#	x_mean[key].plot()

z = calc_comp(x_mean, first_comp, second_comp, third_comp)

for key in z.keys():
	#print(key)
	#print(z[key].index)
	#z[key].plot(linestyle = 'none', marker = 'o')
	fig, ax =  plt.subplots()
	im = ax.imshow(z[key], cmap='RdYlGn')
	ax.set_xticks(np.arange(len(z[key].columns)))
	ax.set_yticks(np.arange(len(z[key].index)))
	ax.set_xticklabels(z[key].columns)
	ax.set_yticklabels(z[key].index)
	plt.colorbar(im)
	plt.title(key)


plt.show()