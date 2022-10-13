

def main():
    money = int(input())
    if money <= 0 or money >= 100:
        print("ошибка")
    elif money == 1 or 21 <= money <= 91:
        print(f"{money} рубль")
    elif 2 <= money <= 4 or 22 <= money <= 94:
        print(f"{money} рубля")
    else:
        print(f"{money} рублей")

main()