string = input("Enter a string: ").strip().lower()
c = 0
flag = True
for i in range(len(string)):
    if string[i] == "o" and c<1:
        c += 1
        flag = False
        print("Found")
if flag:
    print("Not Found")