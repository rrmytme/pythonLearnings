# Unpacks a list
with open("students0.csv") as file:
    for line in file:
        # here we extract multiple values and stores in multiple variables - name, house
        name, house = line.rstrip().split(",")
        print(f"{name} is in {house}")
