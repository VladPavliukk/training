
def main():
    temp_0 = list(map(float, input().split()))
    temp_12 = list(map(float, input().split()))
    avg_temp = float(input())
    error_list = [(temp_0[i] + temp_12[i]) / 2 for i in range(len(temp_0))]

    for i in range(len(error_list)):
        if error_list[i] > avg_temp:
            print(i)
    
main()