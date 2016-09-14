def calcRetirement(birthYear):
    retirementYear = birthYear + 70
    return retirementYear
def main():
    name1 = str(input("Enter name1:"))
    birthYear1 = int(input("Enter birth year:"))
    birthMonth1 = str(input("Enter birth month:"))
    retirementYear1 = calcRetirement(birthYear1)
    
    name2 = str(input("Enter name2:"))
    birthYear2 = int(input("Enter birth year:"))
    birthMonth2 = str(input("Enter birth month:"))
    retirementYear2 = calcRetirement(birthYear2)

    print("", name1, "will become eligible in", birthMonth1,"of",retirementYear1)
    print("", name2, "will become eligible in", birthMonth2,"of",retirementYear2)
main()
