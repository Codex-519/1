number = 0

match number:
    case x if x > 0:
        print("Positive")
    case x if x < 0:
        print("Negative")
    case 0:
        print("Zero")