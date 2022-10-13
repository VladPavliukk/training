

def compute_income(x,k,n):
    s=(x*((1+k/(12*100))**n)) 
    return s

def main():
    x = float(input())

    k = float(input())

    n = int(input())

    result = compute_income(x,k,n)

    print(round(result - x))
    
main()