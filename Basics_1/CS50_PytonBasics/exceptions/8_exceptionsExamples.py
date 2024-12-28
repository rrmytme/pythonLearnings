# Gets a number from the user
x = int(input("What's x? "))
print(f"x is {x}")

# Catches a ValueError
try:
    x = int(input("What's x? "))
    print(f"x is {x}")
except ValueError:
    print("x is not an integer")

# Demonstrates a NameError
try:
    x = int(input("What's x? "))
except ValueError:
    print("x is not an integer")

print(f"x is {x}")

# Demonstrates else
try:
    x = int(input("What's x? "))
except ValueError:
    print("x is not an integer")
else:
    print(f"x is {x}")

# Adds a loop
while True:
    try:
        x = int(input("What's x? "))
    except ValueError:
        print("x is not an integer")
    else:
        break
print(f"x is {x}")

# Adds functions      
def main():
    x = get_int("What's x? ")
    print(f"x is {x}")

# uses break and return
def get_int():
    while True:
        try:
            x = int(input("What's x? "))
        except ValueError:
            print("x is not an integer")
        else:
            break
    return x

# Removes break
def get_int():
    while True:
        try:
            x = int(input("What's x? "))
        except ValueError:
            print("x is not an integer")
        else:
            return x
        
# Removes else 
def get_int():
    while True:
        try:
            return int(input("What's x? "))
        except ValueError:
            print("x is not an integer")   

# Adds pass
def get_int():
    while True:
        try:
            return int(input("What's x? "))
        except ValueError:
            pass    

# Adds prompt
def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            pass      

main()