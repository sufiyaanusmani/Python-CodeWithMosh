from modulefinder import packagePathMap
import random
import string

print(random.random())
print(random.randint(1, 10))
print(random.choice([1, 2, 3, 5]))
print(random.choices([1, 2, 3, 5], k=2))
items = random.choices("abcefghijklmnop", k=4)
p = ""
for item in items:
    p = p + item
print(p)
print(string.ascii_letters)
print("".join(random.choices(string.ascii_letters, k=4)))
numbers = [1, 2, 3, 4]
random.shuffle(numbers)
print(numbers)
random.shuffle(items)
print(p)
p = "".join(items)
print(p)