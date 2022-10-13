

def p_t(t, s, n, k):
    func_p_t = s / n + (s - (t - 1) * s / n) * k / (12 * 100)
    return func_p_t

def main():
    s = int(input())
    n = int(input())
    k = int(input())
    count = 0

    for i in range(1, n + 1):
        result = p_t(i, s, n, k)
        count += result
        print("%2d месяц - %8.2f руб" % (i, result))

    print("Доход банка - %6.2f руб" % (count - s))

main()