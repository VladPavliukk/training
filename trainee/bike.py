
def main():
    minute = list(map(int, input().split()))

    for i in range(len(minute)):
        if minute[i] / 60 >= 12:
            print(i)

if __name__ == "__main__":
    main()