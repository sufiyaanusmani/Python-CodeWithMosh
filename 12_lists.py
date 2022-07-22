# # [] are used for list
# # there can be list of any data type
# letters = ["a", "b", "c"]

# # we can also have list of list
# matrix = [[0, 1], [2, 3]]


# zeros = [0] * 100
# print(zeros)
# combined = zeros + letters
# # list items does not need to be of same type

# numbers = list(range(20))
# print(numbers)

# chars = list("Hello World")
# print(chars)
# print(len(chars))

# # Accessing items
# letters = ["a", "b", "c", "d"]
# print(letters[2])
# print(letters[-1])
# letters[0] = "A"
# print(letters)
# print(letters[1:3])
# print(letters[::2])

# numbers = list(range(20))
# print(numbers)
# print(numbers[::2])
# print(numbers[::-1])


# # List unpacking
# numbers = [1, 2, 3]
# first, second, third = numbers

# num = [1, 2, 3, 4, 4, 5, 6]
# first, second, *other = num
# print(other)    # other is itself a list, same as xargs

# # looping over lists
# letters = ["a", "b", "c"]
# for letter in letters:
#     print(letter)

# for index, letter in enumerate(letters):
#     print(index, letter)

# # Adding or removing items
# letters = ["a", "b", "c"]
# # Add
# letters.append("d")  # append at the end
# letters.insert(0, "-")
# print(letters)

# # Remove
# letters.pop()
# print(letters)
# letters.pop(1)
# print(letters)
# letters.remove("b")
# print(letters)

# # to remove range of items
# del letters[0:3]

# # to remove all items
# letters.clear()

# # Finding Items
# letters = ["a", "b", "c"]
# print(letters.index("b"))

# if "d" in letters:
#     print(letters.index("d"))
# else:
#     print("does not exists")

# print(letters.count("d"))
# print(letters.count("a"))


# # Sorting lists
# numbers = [3, 51, 2, 8, 6]
# numbers.sort()
# print(numbers)
# numbers.sort(reverse=True)
# print(numbers)
# print(sorted(numbers))
# print(sorted(numbers, reverse=True))

# items = [
#     ("Product1", 10),
#     ("Product2", 9),
#     ("Product3", 12),
# ]

# def sort_item(item):
#     return item[1]

# items.sort(key=sort_item)
# print(items)

# # Better method
# items = [
#     ("Product1", 10),
#     ("Product2", 9),
#     ("Product3", 12),
# ]

# # lambda function
# items.sort(key=lambda item:item[1])
# print(items)

# # Map function
# items = [
#     ("Product1", 10),
#     ("Product2", 9),
#     ("Product3", 12),
# ]

# prices = []
# for item in items:
#     prices.append(item[1])

# print(prices)

# x = list(map(lambda item: item[1], items))
# print(x)

# # Filter function
# items = [
#     ("Product1", 10),
#     ("Product2", 9),
#     ("Product3", 12),
# ]

# x = list(filter(lambda item: item[1] >= 10, items))
# print(x)


# # Comprehension
# items = [
#     ("Product1", 10),
#     ("Product2", 9),
#     ("Product3", 12),
# ]

# prices = [item[1] for item in items]    # same as map function

# items = [
#     ("Product1", 10),
#     ("Product2", 9),
#     ("Product3", 12),
# ]

# prices = [item for item in items if item[1] >= 10]    # same as filter function
# print(prices)


# # Zip functions
# list1 = [1, 2, 3]
# list2 = [10, 20, 30]

# print(list(zip(list1, list2)))
# print(list(zip("abc", list1, list2)))
