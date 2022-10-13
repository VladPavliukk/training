

from math import sin, cos, radians
from numpy import array, dot
H, T, t = int(input()), int(input()), float(input())
rotate = array([[cos(radians(360 * t / T)), sin(radians(360 * t / T))], [-sin(radians(360 * t / T)), cos(radians(360 * t / T))]])
position_cabin = array([0, -H / 2])
h = dot(position_cabin, rotate)[1] + (H / 2)
if 0 <= t <= T and T > 0:
    print('Высота = %6.2f м' % (h))
else:
    print('error')