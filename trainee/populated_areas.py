

def main():
    coord_o_x = list(map(int, input().split()))
    coord_o_y = list(map(int, input().split()))
    k = int(input()) 
    n = int(input())

    count = 0

    for i in range(len(coord_o_x)):
        if abs(coord_o_x[i] - coord_o_x[k]) ** 2 + abs(coord_o_y[i] - coord_o_y[k]) ** 2 <= n ** 2:
            count += 1
        
    print(count)
main()
