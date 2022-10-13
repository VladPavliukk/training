import numpy as np

len_main = np.array(list(map(float, input().split())))
high_pyramid = np.array(list(map(float, input().split())))

def volume(a, h):
    vol = (a * a * h) / 3
    return vol


def high(a, h):
    s = 2 * a * np.hypot(a / 2, h)
    return s

def main():
    l = list(volume(len_main, high_pyramid))

    h = list(high(len_main, high_pyramid))

    print("Vmax: %2d, %8.2f, Smin: %2d, %8.2f" % (l.index(max(l)), np.max(l), h.index(min(h)), np.min(h)))

if __name__ == "__main__":
    main()