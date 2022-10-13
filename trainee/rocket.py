from math import sqrt

def volume_pyramid(a, h):
    V = (a ** 2 * h) / (4 * sqrt(3))
    return V

def total_area(a,h):
    S = ((a ** 2 * sqrt(3)) / 4 ) + ((3 * a) / 2) * sqrt(h ** 2 + ((a ** 2) / 12)) 
    return S

def main():
    a = float(input())
    h = float(input())

    if a <= 0 or h <= 0:
        print("error")
    else:

        V = volume_pyramid(a,h)
        S = total_area(a,h)

        print(round(V,3), round(S,3))

main()