# since python has a runtime interpretter we need to define functions or values first before use it 
# to avoid this we use main method 
# Demonstrates defining a main function
def main():
    name = input("What's your name? ")
    hello(name)

# this fn has one parameter called welcomeString and its default value is world
def hello(welcomeString="world"):
    print("hello,", welcomeString)

main()
