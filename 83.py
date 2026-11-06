string = input("Enter a string: ").strip().lower()
i = 0
flag = True
while i < len(string):
    if string[i] == "o":
        print("Found")
        flag = False
    i += 1
if flag:
    print("Not Found")