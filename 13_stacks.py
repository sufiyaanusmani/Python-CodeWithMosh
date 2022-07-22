# LIFO
browsingSesion = []
browsingSesion.append(1)
browsingSesion.append(2)
browsingSesion.append(3)
print(browsingSesion)

browsingSesion.pop()
print(browsingSesion)
current = browsingSesion[-1]
print(current)

if not browsingSesion:
    print("Disable")
else:
    print("Running...")
