import pandas as mypd
# creating a Pandas Series from a dictionary
mydict = {'key1':101, 'key2':102, 'key3':103, 'key4':104, 'key5':105}
mypd_series = mypd.Series(mydict)
print(mypd_series)
