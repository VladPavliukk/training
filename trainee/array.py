import numpy as np

A = list(map(int, input().split()))
B = list(map(int, input().split()))

array_path = np.array(A)
array_speed = np.array(B)

sum_path = np.sum(array_path)

time = array_path / array_speed
sum_time = np.sum(time)

avg_speed = sum_path / sum_time

print("S = %3d км, T = %5.2f час, V = %5.2f км/ч" % (sum_path, sum_time, avg_speed))