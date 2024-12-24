import pandas as mypd
# creating a Pandas Series
mylist = [151, 162, 173, 184, 195]
mypd_series = mypd.Series(mylist, index=['r', 's', 't', 'u', 'v'])
# slicing the Pandas Series using index labels
print(mypd_series['r':'u'])
# slicing the Pandas Series using integer locations
print(mypd_series[1:4])
print(mypd_series.get(10))
print(mypd_series.get('a'))
print(mypd_series.get('a', default=22))
print(mypd_series.get(2, default=32))