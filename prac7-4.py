def timetable():
    number = int(input("Enter the number for timetable:"))
    for i in range (1,11):
     total = number * i
     print(number,"*", i, "=", total)
def main():
    print(timetable())
main()