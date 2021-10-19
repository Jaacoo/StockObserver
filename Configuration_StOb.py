# config file

import pandas as pd

''' Comparing values at given date'''
first_comp = 2 # compare last two available end of day data
second_comp = 7 # compare last available end of data day and seven days ago
third_comp = 30 # compare last available end of day data

with open("NYSE_Symbols.txt") as file:
    nyse_symbs = [line.strip() for line in file]

with open("NASDAQ_Symbols.txt") as f:
    nasdaq_symbs = [line.strip() for line in f]

with open("DAX_Symbols.txt") as f:
    dax_symbs = [line.strip() for line in f]

exchanges_list = ["XETR", "NYSE", "NASDAQ"]
#exchanges_list = ["XETR"]

exch_symbs = {}

for i in exchanges_list:
    exch_symbs[i] = None


exch_symbs["XETR"] = dax_symbs
exch_symbs["NYSE"] = nyse_symbs
exch_symbs["NASDAQ"] = nasdaq_symbs



#for key in exch_symbs.keys():
#    for i in range(len(exch_symbs[key])):
#        print(len(exch_symbs[key]))
#for key, value in exch_symbs.items():
#    print(key, value)
#    print ("End")
