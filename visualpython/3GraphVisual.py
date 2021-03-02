from vpython import *
from vpython import gcurve

string = "yellow: sin^2(x) cyan: cos^2(x), red: sin(x)*cos(x)"
gr = graph(title=string, xtitle="x", ytitle="y")

y1 = gcurve(color=color.yellow)
y2 = gvbars(color=color.cyan)
y3 = gdots(color=color.red)

for x in arange(-5, 5, 0.1):
    y1.plot(pos=(x, sin(x)*sin(x)))
    y2.plot(pos=(x, cos(x)*cos(x)/3))
    y3.plot(pos=(x, sin(x)*cos(x)))
