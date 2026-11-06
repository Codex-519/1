account = "student"
choice = 2
match account:
    case "student":
        match choice:
            case 1:
                print("View Courses")
            case 2:
                print("View Marks")
            case 3:
                print("View Attendance")
            case _:
                print("Invalid Choice")
    case "teacher":
        match choice:
            case 1:
                print("View Students")
            case 2:
                print("Enter Marks")
            case _:
                print("Invalid Choice")
    case _:
        print("Invalid Account Type")