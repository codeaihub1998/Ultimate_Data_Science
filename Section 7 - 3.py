import pandas as mypd
import numpy as mynp
# creating a Pandas Series from a numpy array
myndarray = mynp.array([111,121,131,141,151])
mypd_series = mypd.Series(myndarray)
print(mypd_series)
