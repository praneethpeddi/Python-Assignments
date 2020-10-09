"""Program to add string"""


def add_string():
    """Function that coverts the tuple to list and add the string element"""
    tA = (123, 283)
    lA = list(tA)
    lA.append("String")
    tB = tuple(lA)
    print(tB)


def main():
    """This function calls the function 'add_string'"""
    add_string()


if __name__ == '__main__':
    main()
