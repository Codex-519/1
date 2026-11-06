string = input("Enter a string: ")
result = ""
for ch in string:
    if not ch.isdigit():
        result += ch
print(result)