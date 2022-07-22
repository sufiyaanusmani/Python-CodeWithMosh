# collection of key-value pair
point = {"x": 1, "y": 2}
point = dict(x=1, y=2)
print(point["x"])
point["x"] = 19
print(point)
point["z"] = 30
print(point)
del point["z"]
for x in point:
    print(x, point[x])

for x in point.items():
    print(x)

for key, value in point.items():
    print(key, value)

# Comprehension
values = {x: x * 2 for x in range(5)}
print(values)
