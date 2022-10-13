from math import ceil


def amount_of_paint(a_0, a_1, a_2):
    s = (a_0 ** 2) * 5
    con = a_1 / 1000
    form = ceil(((s * con) / a_2 ))
    return form

def main():
    side_bass = float(input())
    consumption = float(input())
    volume = int(input())

    if side_bass <= 0 or consumption <= 0 or volume <= 0:
        print("error")
    else:
        result = amount_of_paint(side_bass, consumption, volume)
        print(result)

main()
    