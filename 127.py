def book_ticket(source, destination, /, *, passenger, seat="regular"):
    print(source, "to", destination)
    print("Passenger:", passenger)
    print("Seat:", seat)

book_ticket("Pune", "Mumbai", passenger="Asha", seat="window")
book_ticket("Pune", "Mumbai", passenger="Asha")