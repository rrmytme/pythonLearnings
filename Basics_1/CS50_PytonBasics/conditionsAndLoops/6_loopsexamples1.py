# Prints square of bricks using a function with a loop and str multiplication
def main():
    print_square(3)

# range helps to define max boundary value -1 for ex: range(10) = 0 to 9
def print_square(size):
    for _ in range(size):
        print_row(size)


def print_row(width):
    print("#" * width)


main()
