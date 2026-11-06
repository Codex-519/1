total=0
passed=True
grade=""
for i in range(5):
    marks=int(input("Enter marks:"))
    total+=marks
    if marks<35:
        passed=False
percentage=total/5
if passed:
    if percentage>=90:
        grade=("A+")
    elif percentage>=80:
        grade=("A")
    elif percentage>=70:
        grade=("B")
    elif percentage>=60:
        grade=("C")
    elif percentage>=50:
        grade=("D")
    else:
        grade=("E")
else:
    grade=("F")
print("Total marks:",total)
print("Percentage:",percentage)
print("Grade:",grade)
if passed:
    print("PASS")
else:
    print("Fail")