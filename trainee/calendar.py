
def main():
    year = int(input())
    if year < 1582:
        print("error")
    elif year % 4 != 0:
        print(365)
    elif year % 100 != 0:
        print(366)
    elif year % 400 != 0:
        print(365)
    else:
        print(366)

main()