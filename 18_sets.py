# {}
# to prevent dunplication of data
numbers = [1, 1, 2, 3, 4]
uniques = set(numbers)
print(uniques)

second = {1, 4}
second.add(3)
# same functions as list

print(numbers | uniques)  # union
print(numbers & uniques)  # intersection
print(numbers - uniques)
