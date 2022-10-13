import numpy as np


r = np.array(list(map(float, input().split())))
i = np.array(list(map(float, input().split())))

new_list = []

for y in range(len(r)):
    new = 1 / r[y]
    new_list.append(new)

R = 1 / np.sum(new_list)

I = np.sum(i)

U = I * R

print("R = %6.3f Ом, I = %6.3f А, U = %6.3f В"  % (R, I, U))