import numpy as np


x_array = np.array([18.6, 99.9, 157.2, 219.9, 303.7, 399.6, 452.5, 528.4, 613.8, 669.7, 750.6, 816.2, 906.2])

h_array = np.array([85.7, 173.8, 196.7, 259.6, 332.5, 379.3, 414.2, 419.7, 461.3, 438.9, 
 447.8, 434.1, 441.4])

a = np.polyfit(x_array, h_array, 2)
def get_trend(x, a):
    y = a[0] * x **2 + a[1]* x + a[2]
    return y

h_zero = get_trend(0, a)

print("Высота, на которой стоит пушка: %6.2f м" % h_zero)