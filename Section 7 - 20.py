import pandas as mypd
import numpy as mynp
mydf = mypd.Series([120, mypd.NA, mynp.NaN, 125, None])
# arithmetic operations with scalar value
print(mydf*2)
# arithmetic operations between 2 series objects
mys1 = mypd.Series(data = [17,27,37,47,57], index = ['r','s','t','u','v'])
mys2 = mypd.Series(data = [56,57,58,59,60], index = ['r','s','t','u','v'])
print(mys1+mys2)
mys3 = mypd.Series(data = [17,27,37,47,57], index = ['r','s','t','u','v'])
mys4 = mypd.Series(data = [56,57,58,59,60], index = ['r','s','t','w','x'])
print(mys3+mys4)