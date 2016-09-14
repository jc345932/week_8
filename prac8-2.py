def calcAverage(total):
    Average = total / 5
    return Average
def determineGrade(score):
    if score <= 50 :
        print("F")
    elif score <= 64 :
        print("P")
    elif score <= 74 :
        print("C")
    elif score <= 84 :
        print("D")
    else: print("HD")
    return score
def main():
    scores1 = int(input("Enter your score1:"))
    grade = determineGrade(scores1)
    print(grade)
    scores2 = int(input("Enter your score2:"))
    grade = determineGrade(scores2)
    print(grade)
    scores3 = int(input("Enter your score3:"))
    grade = determineGrade(scores3)
    print(grade)
    scores4 = int(input("Enter your score4:"))
    grade = determineGrade(scores4)
    print(grade)
    scores5 = int(input("Enter your score5:"))
    grade = determineGrade(scores5)
    print(grade)
    total = scores1 +scores2 +scores3 +scores4 +scores5
    average = calcAverage(total)
    print("Your average score is:", average)
main()