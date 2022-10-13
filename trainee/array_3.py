import numpy as np

X = list(map(float, input().split()))
Y = list(map(float, input().split()))

x_array = np.array(X)
h_array = np.array(Y)

x_target = float(input())

y_target = float(input())

a = np.polyfit(x_array, h_array, 2)

def get_trend(x, a_0):
    y = a_0[0] * x **2 + a_0[1]* x + a_0[2]
    return y


h_zero = get_trend(0, a)
h_target = get_trend(x_target, a)
delta_h = abs(y_target - h_target)

print(f"h0 = {h_zero:6.2f}, {'yes' if delta_h <= 0.5 else 'no'}")

