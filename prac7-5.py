def value1(obj):
    price1 = (obj * 15)
    return  price1
def value2(obj):
    price2 = (obj * 5)
    return  price2
def value3(obj):
    price3 = (obj * 100)
    return price3
def main():
    shirt = int(input("How many T-shirts do you want?"))
    cup = int(input("How many cups do you want?"))
    drive = int(input("How many Portable hard drives do you want?"))
    shirtPrice = value1(shirt)
    cupPrice = value2(cup)
    drivePrice = value3(drive)
    cost = (shirtPrice) +(cupPrice) +(drivePrice)
    totalItemsCost = (shirt + cup + drive)*3
    if cost < 150:
        totalCost = cost + totalItemsCost
    else: totalCost = cost
    print("Total price is:$", totalCost)
main()