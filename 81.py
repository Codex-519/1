count=0
string = input("Enter a string: ")
for char in string:
    if char == chr(111):  # ASCII value of 'o' is 111
        count+=1
print(f"Total occurrences of 'o': {count}")