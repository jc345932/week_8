#class variable
number = 0

def getValue():
    #local scope
    number = int(input("Enter a value"))
    print(number)

def main():
    print(number)

main()