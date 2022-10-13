
def pd_t(t, s, n, k):
    func_pd_t = s / n + (s - (t - 1) * s / n) * k / (12 * 100)
    return func_pd_t


def pa(ka, n, s):
    func_pa = (ka * (1 + ka) ** n) / ((1 + ka) ** n - 1) * s
    return func_pa
def main():
    s = int(input())
    n = int(input())
    k = int(input())

    summ_s = 0
    summ_a = 0

    ka = k / (12 * 100)

    for i in range(1, n + 1):
        result_dif = pd_t(i, s, n, k)
        result_annu = pa(ka, n, s)

        summ_s += result_dif
        summ_a += result_annu
        
        print("%2d месяц - (диф.) %8.2f руб - (анн.) %8.2f руб" % (i, result_dif, result_annu))

    print("Доход банка - (диф.) %6.2f руб - (анн.) %6.2f руб" % (summ_s - s, summ_a - s)) 