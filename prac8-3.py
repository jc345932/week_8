def main():
    for i in range (1,51,1):
        if i % 3 == 0 :
            print("Fizz")
            if i % 5 ==0:
                print("FizeeBuzz")
        elif i % 5 ==0 :
            print("Buzz")
        else: print(i)
main()


