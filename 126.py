def create_user(name, *, age, city):
    return f"{name}, age {age}, from {city}"

print(create_user("Asha", age=20, city="Pune"))