# config file

import pandas as pd

''' Comparing values at given date'''
first_comp = 2 # compare last two available end of day data
second_comp = 7 # compare last available end of data day and seven days ago
third_comp = 30 # compare last available end of day data

with open("S_P_Symbols.txt") as file:
    s_p_symbs = [line.strip() for line in file]

with open("DAX_Symbols.txt") as f:
    dax_symbs = [line.strip() for line in f]

exchanges = ["NASDAQ", "XETR"]
