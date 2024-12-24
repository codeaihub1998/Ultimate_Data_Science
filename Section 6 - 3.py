import matplotlib.pyplot as myplt
my_cricketers = ['Sachin','Virat','Ricky','Sangakarra','Jacques'] # x-axis values
my_centuries = [100,76,71,63,62] #height of bars, y-axis values
mywidthlist= [0.9,0.8,0.7,0.6,0.5]
myplt.bar(my_cricketers,my_centuries,width = mywidthlist)
myplt.xlabel('Cricketer Name',color='b',fontsize=15)
myplt.ylabel('Number of Centuries',color='g',fontsize=15)
myplt.title('Cricketer wise number of centuries',color='r',fontsize=15)
myplt.show()