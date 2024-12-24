import pandas as mypd

# creating a Pandas Series
mylist = [111, 112, 113, 114, 115]
mypd_series = mypd.Series(mylist, index=['r', 's', 't', 'u', 'v'])
# filtering the Pandas Series using Boolean indexing
my_bool_filter = mypd_series > 3
my_filtered_mypdseries = mypd_series[my_bool_filter]
print(my_filtered_mypdseries)
