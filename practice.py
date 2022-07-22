# st = "This  is a text"
# if "  " in st:
#     print("Yes")
#     newSt = st.replace("  ", " ")
# else:
#     print("No")

# print(st)
# print(newSt)

# items = []
# while True:
#     item = input(">>> ")
#     if(item.lower() == "quit"):
#         break
#     else:
#         items.append(item)

# print(items)

# marks = []
# for i in range(5):
#     mark = int(input(f"Enter marks for subject {i+1}: "))
#     marks.append(mark)

# marks.sort()
# print(marks)

# lst = [2, 4, 5, 9]
# s = 0
# for item in lst:
#     s += item

# print(s)

# a = (7, 0, 8, 0, 0, 9)
# count = 0

# for number in a:
#     if number == 0:
#         count += 1

# print(count)

# languages = {
#     "web": "HTML, CSS, JS",
#     "sys": "C, C++",
#     "ml": "Python",
#     "GUI": "C#, Python, Java"
# }

# print(languages)

# numbers = []
# for i in range(8):
#     num = int(input("Enter a number: "))
#     numbers.append(num)

# uniques = set(numbers)
# print(uniques)

# numbers = []
# for i in range(4):
#     num = int(input("Enter a number: "))
#     numbers.append(num)

# numbers.sort()
# print(numbers[-1])


# username = input("Enter your username: ")
# if len(username) < 10:
#     print("Less than 10")
# else:
#     print(">= 10")

# num = int(input("Enter a number to print its multiplication table: "))
# for i in range(10):
#     print(f"{num} x {i+1} = {num * (i+1)}")

# def greatest(num1, num2, num3):
#     numbers = []
#     numbers.append(num1)
#     numbers.append(num2)
#     numbers.append(num3)
#     numbers.sort()
#     return numbers[-1]

# print(greatest(4, 5, 2))

# class Student:
#     def __init__(self, name, gpa):
#         self.name = name
#         self.__setGpa(gpa)

#     def __setGpa(self, gpa):
#         if gpa < 0:
#             print("GPA can not be negative")
#         else:
#             self.__gpa = gpa

#     def __getGpa(self):
#         return f"GPA: {self.__gpa}"

#     gpa = property(__getGpa, __setGpa)


# student = Student("Sufiyaan", 4.0)  
# print(student.gpa)  
