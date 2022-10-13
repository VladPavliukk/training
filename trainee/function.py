from math import atan, pi

def arc_catan(x):
    return pi/2 - atan(x)

def n_t(t):
    func_n_t = 172 / 45 * arc_catan((2000 - t) / 45)
    return func_n_t

def main():
    list_x = []
    n = int(input())
    for i in range(n):
        year = int(input())
        list_x.append(year)
    for y in list_x:
        result = n_t(y)
        print(f"x {y} = {round(result, 3)}")
main()

