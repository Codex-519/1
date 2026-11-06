# Take 2 no. from user.
# Show operation menu to user.
# Read a choice of operation.
#Perfrom operation using match case and display output.

a=float(input("Enter First no. :"))
b=float(input("Enter Second no. :"))

print("\nOperation Menu")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

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
    case _:
        print("Invalid choice")