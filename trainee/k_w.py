def main():
    intake = list(map(int, input().split()))
    normal = int(input())
    price_normal = float(input())
    price_over = float(input())
    count = 0

    for i in intake:
        if i > normal:
            count = count + normal * price_normal + (i - normal) * price_over
        else:
            count += i * price_normal
        
    print("Сумма: %6d кВт ч, стоимость %7.2f руб" % (sum(intake), count))

main()