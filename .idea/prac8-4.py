def main():
    password = str(input("Enter your password:"))
    check(password)
def check(length):
    if len(length) >= 7:
        print("The password is valid")
    else: print("Your must try again!")
main()