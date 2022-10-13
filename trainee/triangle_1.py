import math

def len_side(x_0, y_0, x_1, y_1):
    len_line = math.sqrt((x_0 - x_1) ** 2 + (y_0 - y_1) ** 2)
    return len_line

def triangle_area(a_1, a_2, a_3):
    p = a_1 + a_2 + a_3

    s = math.sqrt(p/2 * (p/2 - a_1) * (p/2 - a_2) * (p/2 - a_3))
    return s


def triangle_deegres(a_1, a_2, a_3):

    tria_deg = math.acos((a_1 ** 2 + a_2 ** 2 - a_3 ** 2) / (2 * a_1 * a_2))
    return math.degrees(tria_deg)

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
    
    if check_true(a, b, c) == False:
        print("Трикутника не існує")
    else:
        s = triangle_area(a,b,c)
        p = a + b + c

        angle_A = triangle_deegres(c,b,a)
        angle_B = triangle_deegres(c,a,b)
        angle_C = triangle_deegres(a,b,c)
    
        print(f"Сторони: {round(a,3), round(b,3), round(c,3)}")

        print(f"Площадь : {round(s,3)}")

        print(f"Периметр : {round(p,3)}")

        print(f"Угли : {round(angle_A, 3), round(angle_B, 3), round(angle_C, 3)}")
 

main()