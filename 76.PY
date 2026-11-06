while True:
    a = float(input("Enter First no. : "))
    b = float(input("Enter Second no. : "))

    print("\nOperation Menu")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("0. Exit")

    choice = int(input("Enter your choice: "))

    match choice:
        case 1:
            print("Result =", a + b)
        case 2:
            print("Result =", a - b)
        case 3:
            print("Result =", a * b)
        case 4:
            if b != 0:
                print("Result =", a / b)
            else:
                print("Cannot divide by zero")
        case 0:
            print("Program Ended")
            break
        case _:
            print("Invalid choice")