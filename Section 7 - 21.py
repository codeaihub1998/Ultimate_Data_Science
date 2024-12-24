import pandas as mypd
import numpy as mynp
mys1 = mypd.Series(data = [31,32,33,34,35,mynp.NaN], index = ['r','s','t','u','v','y'])
mys2 = mypd.Series(data = [36,37,38,39,40], index = ['r','s','t','w','x'])
print(mys1.add(mys2, fill_value=0))