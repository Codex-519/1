while True:
    number = int(input("Enter a number (0 to stop): "))
    if number == 0:
        print("Stopping the input.")
        break 
    else:
        print(f"You entered: {number}")