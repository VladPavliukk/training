
def compute_income(x,k,n):
    s=(x*((1+k/(12*100))**n)) 
    return s

def main():
    profit = float(input())

    k = float(input())

    month = int(input()) 
    bank = 0

    for i in range(0, 40000):
        income = compute_income(i, k, month)
        if round(income) - i == profit:
            bank = i
    
    print(bank)

main()