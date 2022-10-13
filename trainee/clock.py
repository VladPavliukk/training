
def degrees_of_clock(a_0, a_1, a_2):

    degrees_h = 360 / 12 * a_0
    degrees_m = 30 / 60 * a_1
    degrees_s = 0.5 / 60 * a_2
    
    result = degrees_h + degrees_m + degrees_s
    return result

def main():

    h = int(input())
    m = int(input())
    s = int(input())

    if h == 12 or h < 0 or m == 60 or m < 0 or s == 60 or s < 0:
        print("error")
    else:
        result = degrees_of_clock(h,m,s)
        print(round(result, 2))
main()