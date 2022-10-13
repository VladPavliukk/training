import math


def len_side(x_0, y_0, x_1, y_1):
    len_line = math.sqrt((x_0 - x_1) ** 2 + (y_0 - y_1) ** 2)
    return len_line

def circle_radius(a_0,a_1,a_2):
    p = a_0 + a_1 + a_2
    r = math.sqrt((((p/2) - a_0) * ((p/2) - a_1) * ((p/2) - a_2)) / (p/2))

    return r

def circle_radius_m(a_0, a_1, a_2):
    p = a_0 + a_1 + a_2
    s = math.sqrt(p/2 * (p/2 - a_0) * (p/2 - a_1) * (p/2 - a_2))
    R = (a_0 * a_1 * a_2) / (4 * s)
    return R

def triangle_median(a_1, a_2, a_3):
    M = (1/2) * math.sqrt(2 * (a_1 ** 2 + a_2 ** 2) - a_3 ** 2)
    return M

def check_true(a, b, c):
    if a + b <= c or b + c <= a or a + c <= b:
        return False
    else:
        return True


def main():

    x_a, y_a, x_b, y_b, x_c, y_c = map(float, input("x_a, y_a, x_b, y_b, x_c, y_c \n").split())

    c = len_side(x_a, y_a, x_b, y_b)
    a = len_side(x_b, y_b, x_c, y_c)
    b = len_side(x_a, y_a, x_c, y_c)

    if check_true(a,b,c) == False:
        print("error")
    else:
        radius = circle_radius(a,b,c)
        radius_M = circle_radius_m(a,b,c)
        M_a = triangle_median(c,b,a)
        M_b = triangle_median(a,c,b)
        M_c = triangle_median(a,b,c)

        print(f"Радіус = {round(radius, 4)}, Радіус R = {round(radius_M, 4)}, Сума медіан = {round(M_a + M_b + M_c, 4)}" , end = " ")
        
    

main()