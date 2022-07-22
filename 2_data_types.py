import math

studentCount = 1000 # int
print(studentCount)

rating = 4.99 # float
isPublished = True # boolean
courseName = "Python Programming" # string


# Strings
course = "Python Programming"
message = """
Dear Sufiyaan,
    blah blah blah
Regards,
    Anonymous
"""     # Formatted String (will store as it is)

print(len(course))
print(course[0])
print(course[3])
print(course[-1])
print(course[0:3])
print(course[4:])
print(course[:8])
print(course[:])

# Escape Sequence
name = "Sufiyaan \"Usmani\""
print(name)


first = "Sufiyaan"
last = "Usmani"
full = first + " " + last
print(full)
# although above method is ok, but we can also use formatted string
fullName = f"{first} {last}" # f stands for formatted
print(fullName)

# String methods
print(course.upper())
print(course.lower())
print(course.title()) # capitlizes first letter of every word
print(course.strip()) # removes whitespaces from the beginning and end of the string
print(course.lstrip()) # removes whitespaces from the beginning of the string
print(course.rstrip()) # removes whitespaces from the end of the string
print(course.find("Pro"))
print(course.replace("P", "$"))
print("Pro" in course)
print("Java" in course)
print("Java" not in course)

# Numbers
print(round(2.8))
print(abs(-3.3))
print(math.ceil(4.3))

n = input("Enter n: ")
# input() function always return string
# So, for numbers, we first need to convert our input string to number
# int(x)
# float(x)
# bool(x)
# str(x)
print(type(n))
print(int(n) + 2)

# Falsy values (values considered as boolean False)
# ""   : False
# 0    : False
# None : False
# Anything else will be True
