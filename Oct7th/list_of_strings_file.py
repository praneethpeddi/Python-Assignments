"""Program to print list of data from a text file"""


def list_string(file):
    """This function prints a list of data from a text file"""
    with open(file) as file_1:
        data = file_1.readlines()
        print(data)


def main():
    """This function calls a function"""
    filename = '1log.txt'
    list_string(filename)


if __name__ == '__main__':
    main()
