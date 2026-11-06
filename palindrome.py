string = input("Enter a string: ")
start = 0
end = len(string) - 1
palindrome = True
while start < end:
    if string[start] != string[end]:
        palindrome = False
        break
    start += 1
    end -= 1
if palindrome:
    print("Palindrome")
else:
    print("Not Palindrome")