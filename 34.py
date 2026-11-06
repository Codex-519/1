Name=input("Enter a name : ").strip().lower()
length=len(Name)
sum=" "
for number in range(length-1,-1,-1):
    sum=sum+Name[number]
if Name==sum:
    print(Name,"is a Palindrome!!")
else:
    print(Name,"is not a Palindrome !!")