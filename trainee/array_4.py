import numpy as np

def get_trend_poli_1(x, a_0):
    y = a_0[0] *x + a_0[1]
    return y

def get_trend_poli_2(x, b_0):
    y = b_0[0] * x **2 + b_0[1]* x + b_0[2]
    return y

def error(x, x_r):
    err = abs((x - x_r) / x_r) * 100
    return err
def main():
    X = list(map(float, input().split()))
    Y = list(map(float, input().split()))

    x_array = np.array(X)
    y_array = np.array(Y)

    a = np.polyfit(x_array, y_array, 1)
    b = np.polyfit(x_array, y_array, 2)

    trand_1 = get_trend_poli_1(x_array, a)
    trand_2 = get_trend_poli_2(x_array, b)

    error_trand_1 = error(y_array, trand_1)
    error_trand_2 = error(y_array, trand_2)

    avg_error = np.mean(error_trand_1)
    avg_error_2 = np.mean(error_trand_2)

    if avg_error >= avg_error_2:
        print('{:.3f} {:.3f} {:.3f}'.format(b[0], b[1], b[2]))
    else:
        print('{:.3f} {:.3f}'.format(a[0], a[1]))
    
main()
