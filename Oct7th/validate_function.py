"""Program to validate a function is_prime"""


def is_prime(num):
    """This function will return True if a number is Prime"""
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                return False
        else:
            return True


def main():
    """This is a function which validates the is_prime function"""
    inputs = [(100, False), (21, False), (30, False), (19, True), (37, True), (25, False)]
    for i in inputs:
        actual = is_prime(i[0])
        if i[1] == actual:
            print(f"Validation with the number {i[0]} returned the expected value {i[1]}: Success")
        else:
            print(f"Validation with the number {i[0]} not returned the expected value {i[1]}: Failed")


if __name__ == '__main__':
    main()
