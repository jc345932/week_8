nameList = []
def name():
    for name in nameList:
         print(name)

def main():
    for i in range (3):
        user_input = input("Enter the name:")
        nameList.append(user_input)
    name()
main()