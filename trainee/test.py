# import math


# x_a = float(input())
# y_a = float(input())
# x_b = float(input())
# y_b = float(input())
# x_c = float(input())
# y_c = float(input())


# def len_side(x_0, y_0, x_1, y_1):
#     len_line = math.sqrt((x_0 - x_1) ** 2 + (y_0 - y_1) ** 2)
#     return len_line

# c = len_side(x_a, y_a, x_b, y_b)
# a = len_side(x_b, y_b, x_c, y_c)
# b = len_side(x_a, y_a, x_c, y_c)

# print(round(c,4),round(a,4),round(b,4))
# p = a + b + c 
# print(round(p, 4))

# r = math.sqrt((((p/2) - a) * ((p/2) - b) * ((p/2) - c)) / (p/2))
# print(round(r, 4))

# s = math.sqrt(p/2 * (p/2 - a) * (p/2 - b) * (p/2 - c))

# R = (a * b * c) / (4 * s)
# print(round(R, 4))

# def triangle_median(a_1, a_2, a_3):
#     M = (1/2) * math.sqrt(2 * (a_1 ** 2 + a_2 ** 2) - a_3 ** 2)
#     return M

# M_a = triangle_median(c,b,a)
# M_b = triangle_median(a,c,b)
# M_c = triangle_median(a,b,c)

# print(round(M_a, 4), round(M_b, 4), round(M_c, 4))    

