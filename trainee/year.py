from math import atan, pi

def arc_catan(x):
    return pi/2 - atan(x)

def n_t(t):
    func_n_t = 172 / 45 * arc_catan((2000 - t) / 45)
    return func_n_t

years = [1000, 1750, 1800, 1850, 1900, 1950, 1955, 
         1960, 1965, 1970, 1975, 1980, 1985, 1990, 1995, 
         2000, 2005, 2010, 2011, 2012, 2013, 2014, 2015,
         2016, 2017, 2018, 2019]

population =[0.400, 0.791, 1.000, 1.262, 1.650, 2.519,
             2.756, 3.021, 3.335, 3.692, 4.068, 4.435, 4.831,
             5.264, 5.674, 6.071, 6.344, 6.933, 7.015, 7.100,
             7.162, 7.271, 7.358, 7.444, 7.530, 7.669, 7.763]  
def main():
    n_1 = int(input())
    n_2 = int(input())
    new_list = []
    for i in years:
        new_list.append(n_t(i))
    
    error_list = [abs((population[i] - new_list[i]) / population[i]) for i in range(len(years))]
    max_error = max(error_list[n_1 : n_2 + 1])
    index_max_error = error_list.index(max_error)

    min_error = min(error_list[n_1 : n_2 + 1])
    index_min_error = error_list.index(min_error)

    avg_error = sum(error_list[n_1 : n_2 + 1]) / len(years[n_1 : n_2 + 1]) * 100

    print(f"Погрешность - минимальная, год: {years[index_min_error]}, максимальная, год: {years[index_max_error]}, средняя, процент: {round(avg_error, 3)}")
        
main()