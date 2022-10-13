import numpy as np
from math import sqrt

n = int(input())
points = []


for i in range(n):
    line = input()
    new_line = line.split()
    points.append(new_line)

points_array = np.array(points, dtype = float)
avg = np.mean(points_array, 0)
sx = avg[0]
sy = avg[1]
array_list2 = []
t = 0
for i in range(n):
    d = points_array[t]
    d = sqrt(((d[0]-avg[0])**2)+((d[1]-avg[1])**2))
    array_list2.append(d)
    t = t+1

radius = np.array(array_list2, dtype=float)
r = radius.max()

print("центр в точке (%6.3f, %6.3f), r = %6.3f" % (sx, sy, r))
