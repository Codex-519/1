# def check():
#     print("Before return")
#     return 10
#     print("After return")

# value = check()
# print(value)

def double(number):
    return number * 2

def add_five(number):
    return number + 5

result = add_five(double(10))
print(result)