string = input("Enter a string: ")
count = 0
for ch in string:
    if ch.islower():
        count += 1
print(count)