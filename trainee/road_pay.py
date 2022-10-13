import numpy as np

len_road = np.array(list(map(int, input().split())))
avg_car = list(map(int, input().split()))

result_len_road = np.sum(len_road)

price = 0

c = np.array([])

c = avg_car / len_road

for i in c:
    if i <= 30:
        price += 1
    elif 31 <= i <= 60:
        price += 1.5
    elif 61 <= i <= 120:
        price += 3
    else:
        price += 4.5
    
print("Длина пути: %3d км, оплата: %5.2f S$" % (result_len_road, price))