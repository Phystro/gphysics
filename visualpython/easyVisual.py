# Simple graph object using visual python

from vpython import *

gr1 = graph( width=600, height=450,\
        title="Visual 2D graph", xtitle="x", ytitle="f(x)",\
        foreground=color.black, background=color.white)

plot1 = gcurve(color = color.cyan)

for x in arange(0.0, 8.1, 0.1):
    plot1.plot(pos=(x, 5.0 * cos(2.0 * x) * exp(-0.4 * x) )) # plot the points



gr2 = graph( width=600, height=450,\
        title="Visual 2D graph", xtitle="x", ytitle="f(x)",\
        foreground=color.black, background=color.white)

plot2 = gdots(color = color.black)

for x in arange(-5.0, 5.0, 0.1):
    plot2.plot( pos = (x, cos(x)) )


