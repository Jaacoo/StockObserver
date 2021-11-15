# config file

import pandas as pd


''' Comparing values at given date'''
first_comp = 2 # compare last two available end of day data
second_comp = 7 # compare last available end of data day and seven days ago
third_comp = 30 # compare last available end of day data and thirty days ago

rolling_window = 4

with open("NYSE_Symbols_test.txt") as file:
    nyse_symbs = [line.strip() for line in file]

with open("NASDAQ_Symbols_test.txt") as f:
    nasdaq_symbs = [line.strip() for line in f]

with open("DAX_Symbols_test.txt") as f:
    dax_symbs = [line.strip() for line in f]

exchanges_list = ["XETR", "NYSE", "NASDAQ"]

exch_symbs = {}

for i in exchanges_list:
    exch_symbs[i] = None


exch_symbs["XETR"] = dax_symbs
exch_symbs["NYSE"] = nyse_symbs
exch_symbs["NASDAQ"] = nasdaq_symbs