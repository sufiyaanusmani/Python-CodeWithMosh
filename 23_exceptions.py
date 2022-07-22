# try:
#     age = int(input("Enter your age: "))
# except ValueError as ex:  # writing as ex is optional
#     print("Invalid age entered")
#     print(ex)
# else:   # optional
#     print("No exceptions were thrown")

# print("Always runs")


# try:
#     age = int(input("Enter your age: "))
#     xfactor = 10 / age
# except ValueError:
#     print("Invalid age entered")
# except ZeroDivisionError:
#     print("Number can not be divided by Zero")
# else:  # only runs if no exceptions were thrown
#     print("No exceptions were thrown")
# print("Outside try-except block")


# try:
#     age = int(input("Enter your age: "))
#     xfactor = 10 / age
# except (ValueError, ZeroDivisionError):
#     print("Invalid age entered")
# else:
#     print("No exceptions were thrown")

# try:
#     file = open("1_first.py")
#     age = int(input("Enter your age: "))
#     xfactor = 10 / age
# except (ValueError, ZeroDivisionError):
#     print("Invalid age entered")
# else:
#     print("No exceptions were thrown")
# finally: # it is always executed wheter exception occurs or not
#     file.close()


# try:
#     with open("app.py") as file, open("another.txt") as target: # no need to close file, it will close by itself
#         print("File opened")
#     age = int(input("Enter your age: "))
#     xfactor = 10 / age
# except (ValueError, ZeroDivisionError):
#     print("Invalid age entered")
# else:
#     print("No exceptions were thrown")

# def calculate(age):
#     if age <= 0:
#         raise ValueError("Age can not be 0 or less")
#     return 10 / age


# try:
#     calculate(0)
# except ValueError as error:
#     print(error)


from timeit import timeit

code1 = """
def calculate(age):
    if age <= 0:
        raise ValueError("Age can not be 0 or less")
    return 10 / age


try:
    calculate(0)
except ValueError as error:
    pass
"""

code2 = """
def calculate(age):
    if age <= 0:
        return None
    return 10 / age


    f = calculate(0)
    if f == None:
        pass
"""

print("First Code: ", timeit(code1, number=100000))
print("Second Code: ", timeit(code2, number=100000))