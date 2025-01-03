# Sorts a list of dictionaries using a lambda function
students = []

with open("students0.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        students.append({"name": name, "house": house})
'''
lambda function is a anonymous function 
which is equivalent to 
def get_name(student):
    return student["name"] 
'''
for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} is in {student['house']}")
