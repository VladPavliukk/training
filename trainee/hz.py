def compute_income(d, r, m):
    res = d * (1 + r / (12 * 100))**m
    return round(res)

res_inc = 658
mon = 8
rate = 7
res_depos = 0

for depos in range(0, 40000):
    inc = compute_income(depos, rate, mon) - depos
    if int(inc) == res_inc:
        res_depos = depos

print(res_depos)