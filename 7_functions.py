# def greet():
#     print("Hi there")
#     print("Welcome")


# # calling function
# greet()


# def greet(firstName, lastName):
#     print(f"Hi {firstName} {lastName}")
#     print("Welcome")


# # calling function
# greet("Sufiyaan", "Usmani")


# # Keyword arguments
# def increment(num, by):
#     return num + by


# # we use keyword arguments to make our code more readable
# print(increment(3, by=2))


# Default Arguments
def increment(num, by=1):
    return num + by


print(increment(2))
print(increment(2, 5))
