import numpy as np

country = str(input())

people = np.array(input().split(), dtype=float)

years = np.array([int(x) for x in range(2005, 2018, 1)])

degree_of_the_polynomial = int(input())

number_of_turists_in_2018 = float(input())


def get_trend(x, a, deg):
    if deg == 1:
        y = a[0] * x + a[1]
        return y
    elif deg == 2:
        y = a[0] * x**2 + a[1] * x + a[2]
        return y
    else:
        y = a[0] * x**3 + a[1] * x**2 + a[2] * x + a[3]
        return y
    


def error(x, x_r):
    err = abs((x - x_r) / x_r) * 100
    return err

a = np.polyfit(years, people , degree_of_the_polynomial)
result = get_trend(2018, a, degree_of_the_polynomial)

error_rate = error(result, number_of_turists_in_2018)
print("Страна:%6s, прогноз:%6.3fмлн чел, относительная погрешность:%4.2fпроц." % (country, result, error_rate))