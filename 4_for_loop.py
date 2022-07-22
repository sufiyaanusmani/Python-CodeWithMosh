for i in range(3):
    print(f"Attempt {i+1}: Sending...")


for i in range(1, 4):
    print(f"Attempt {i}: Sending...")


for i in range(1, 10, 2):
    print(f"Attempt {i}: Sending...")


successful = True
for i in range(3):
    print(f"Attempt {i+1}: Sending...")
    if(successful):
        print("Successful")
        break

# Nested loop
for i in range(5):
    for j in range(3):
        print(f"({i}, {j})")


# Strings
for ch in "Python":
    print(ch)
