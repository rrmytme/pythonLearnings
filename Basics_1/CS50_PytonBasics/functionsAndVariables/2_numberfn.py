# Demonstrates conversion from str to int
x = input("What's x? ")
y = input("What's y? ")
z = int(x) + int(y)
print(z)

# Demonstrates nesting of function calls
x = int(input("What's integer x? "))
y = int(input("What's integer y? "))
z = x + y
print(z)

# Demonstrates conversion of str to float
x = float(input("What's float x? "))
y = float(input("What's float y? "))
z = x + y
print(z)

# Demonstrates rounding to nearest int
z = round(x + y)
print(z)

# Demonstrates fewer variables
print(round(x + y))

# Demonstrates formatting with commas ex:1,000
z = round(x + y)
print(f"{z:,}")

# Demonstrates simple division
z = x / y
print(z)

# Demonstrates rounding after the decimal point
z = round(x / y, 2)
print(z)

# Demonstrates formatting after the decimal place
z = x / y
print(f"{z:.2f}")

