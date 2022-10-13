from math import atan, pi

def arc_catan(x):
    return pi/2 - atan(x)

def n_t(t):
    func_n_t = 172 / 45 * arc_catan((2000 - t) / 45)
    return func_n_t

def main():
    n = input().split()
    x_list = [int(x) for x in n]
    for y in x_list:
        result = n_t(y)
        print ("%5d - %6.3f миллиард(ов)" % (y, result))


main()