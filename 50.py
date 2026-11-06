num = int(input("Enter a no. : "))

for i in range(1, num + 1):
    if i == num // 2:
        print("*" + " " * (num - 3) + "*  *")
    elif i == num:
        print("*" * num)
    else:
        print("*" + " " * (num - 2) + "*")