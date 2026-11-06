string = input("Enter a string: ").strip().lower()
reverse = ""
for i in range(len(string) - 1, -1, -1):
    reverse = reverse + string[i]
if string == reverse:
    print(string,"is a Palindrome!!")
else:
    print(string,"is not a Palindrome!!")