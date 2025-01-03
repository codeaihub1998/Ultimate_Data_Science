import numpy as mynp
# print(help(mynp.append))
myarr1 = mynp.arange(10)
print("In 1-D array, since element added is of float type, all the elements will be converted to float type")
myarr2 = mynp.append(myarr1, 10.5)
print(myarr2)
myarr3 = mynp.append(myarr1, '10.5')
print(myarr3)
print("2-D array: axis is not specified. So will flattened to 1-D array")
myarr4 = mynp.arange(6).reshape(2,3)
myarr5 = mynp.append(myarr4,10)
print(myarr5)
print("If I/P array is 2-D array and axis is specified, then appended array must also be 2-D array otherwise error")
myarr6 = mynp.arange(10,16).reshape(2,3)
myarr7 = mynp.append(myarr4,myarr6, axis=0)
print(myarr7)
print("appending to columns for 2-D array")
myarr8 = mynp.append(myarr4,myarr6, axis=1)
print(myarr8)