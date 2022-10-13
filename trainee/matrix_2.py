import math as mt
import numpy as np


def main_rotate(angle):
    func = [[mt.cos(mt.radians(angle)), mt.sin(mt.radians(angle))],[-mt.sin(mt.radians(angle)), mt.cos(mt.radians(angle))]]
    return func

n = int(input())
new_list = []
for i in range(0, n):
    new = input()
    array_str = new.split()
    new_list.append(array_str)

new_array = np.array(new_list, dtype=int)

angle = int(input())
rotate = np.array(main_rotate(angle))

coord = np.dot(new_array, rotate)
avg = np.mean(coord, 0)

print("avg_x = %6.2f, avg_y = %6.2f" % (np.round(avg[0], 2), np.round(avg[1], 2)))

