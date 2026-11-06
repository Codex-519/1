def calculate(a, b, /, operation="add"):
    if operation == "add":
        return a + b
    if operation == "multiply":
        return a * b
    return None

print(calculate(3, 4))
print(calculate(3, 4, operation="multiply"))