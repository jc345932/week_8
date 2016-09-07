def value(shirt):
    shirtprice = shirt * 15
    return  shirtprice
def value(cup):
    cupprice = cup * 5
    return  cupprice
def value(drive):
    driveprice = drive * 100
    return driveprice
def main():
    shirt = int(input("How many T-shirts do you want?"))
    cup = int(input("How many cups do you want?"))
    drive = int(input("How many Portable hard drives do you want?"))
    total = value(shirt)+ value(cup)+ value(drive)
    print("Total price is:$", total)
main()