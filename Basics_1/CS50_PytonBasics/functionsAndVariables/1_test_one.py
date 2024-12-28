# if a is string then 
# a.strip() - remove all white spaces
# a.capitalize - sentences first word's first letter become capital
# a.title - sentences all word's first letter become capital(camel case)
a = input("Hi enter something:").strip().title()

# by default the input method take string hence we convert that to int() like below
b = int(input("Hi enter one more thing:"))
print("you entered:", a, b)

# below print statement is same as above except the syntax
#f string is comes wit latest pyton versions to handle formatting effieciently  
print(f"you entered: {a}, {b}")

c = b+6
print(f"the answer is: {c}")