temperature = 35

if temperature > 30:
    print("It's warm")
    print("Drink Water")
elif temperature > 15:
    print("It's nice")
else:
    print("It's cold")
print("Done")


# Ternary operator
age = 22
message = "Eligible" if age >= 18 else "Not eligible"
print(message)


# Chaining Comparison Operators

# Normal way
if age >= 18 and age < 65:
    print("Eligible")
else:
    print("Not eligible")

# Chaining
if 18 <= age < 65:
    print("Eligible")
else:
    print("Not eligible")
