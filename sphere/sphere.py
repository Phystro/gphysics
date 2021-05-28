from __future__ import division
from vpython import *
import vpython as vp
import numpy as np

s = sphere(pos=vector(10, 5, 0), radius=100.10)
for theta in np.arange(0, 10*np.pi, 0.1):
    rate(30)
    x = np.cos(theta)
    y = np.sin(theta)
    s.pos = 100 * vector(x, y, 0)

    print(s.pos)


