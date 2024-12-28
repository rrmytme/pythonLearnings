# Reads from a file

with open("names.txt") as file:
    lines = file.readlines()
# rstrip() method remove all white spaces
for line in lines:
    print("hello,", line.rstrip())
