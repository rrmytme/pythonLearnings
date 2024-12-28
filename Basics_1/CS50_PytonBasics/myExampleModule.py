# sample module will use the methods within in it from other program
def main():
    hello("world")
    goodbye("world")


def hello(name):
    print(f"hello, {name}")


def goodbye(name):
    print(f"goodbye, {name}")

# Check __name__  helps to tell te python interpreter that we call main metod only when directly execute this proram
if __name__ == "__main__":
    main()
