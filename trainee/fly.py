
def main():
    price_fly = (float(input()) * 3)
    price_gas = float(input())
    distance = float(input())

    price_car = ((0.12 * distance) * price_gas) * 2

    if price_fly <= 0 or price_gas <= 0 or distance <= 0:
        print("error")
    elif price_car > price_fly:
        print(round(price_fly,2))
    else:
        print(round(price_car, 2)) 
    
if __name__ == "__main__":
    main()