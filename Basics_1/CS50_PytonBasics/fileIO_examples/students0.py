# Reads a CSV file, default file mode is -r read hence we dont need to explicitly mention that

with open("students0.csv") as file:
    for line in file:
        # split(",") metod splits te values in a row using specific seperator in this case its ","
        row = line.rstrip().split(",")
        print(f"{row[0]} is in {row[1]}")
