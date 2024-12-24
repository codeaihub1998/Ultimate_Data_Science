# mfc property
import matplotlib.pyplot as myplt
import numpy as mynp
x_axis = mynp.arange(1,11)
y_axis = x_axis**3
myplt.plot(x_axis,y_axis,'o:g', lw=5, ms = 10, mfc='yellow')
myplt.title('Cube Function Line Plot')
myplt.xlabel('X axis-Value -------')
myplt.ylabel('Cube of Y axis-Value -------')
myplt.show()
