"""Program to validate the data types"""


def datatype_validation(inputs):
    """checking the data types"""
    print(type(inputs))


def main():
    """Function that passes the different data types"""
    inputting = [5, 6, 'string', 5.7, ]
    for i in inputting:
        datatype_validation(i)


if __name__ == "__main__":
    main()
