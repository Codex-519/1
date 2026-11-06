gas_booking = input("Do you want to book gas? (yes/no): ")
match gas_booking:
    case "yes":
        payment = input("Payment done? (yes/no): ")
        match payment:
            case "yes":
                print("Gas booking is confirmed.")
            case "no":
                print("Please complete the payment.")
            case _:
                print("Invalid payment input.")
    case "no":
        print("Gas booking is not confirmed.")
    case _:
        print("Invalid input.")