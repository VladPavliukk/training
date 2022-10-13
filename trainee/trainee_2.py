import math

x = float(input())

y = float(input())

x_2 = x ** 2

y_2 = y ** 2

form = x_2 + y_2 + 1

z = math.asin(math.cos(x + math.sqrt(3)/2* math.pi) )+1.2 * math.sqrt(2 - (math.cos(y))**2) 

z_f = z / form
 
print(round(z_f, 5))
