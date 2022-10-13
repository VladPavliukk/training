import numpy as np

def get_trend(x, a_0):
    y = a_0[0] * x **2 + a_0[1]* x + a_0[2]
    return y

def main():
    x = np.array(list(map(int, input().split())))
    y = np.array(list(map(float, input().split())))
    angle = int(input())

    poly = np.polyfit(x, y, 2)

    result = get_trend(angle, poly)
    print("Дальность: %6.2f м" % (result))

if __name__ == "__main__":
    main()