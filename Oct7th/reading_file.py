"""Reading the entire and printing the content of the file"""


def reading_file(file):
    """This function reads the entire content of file"""
    with open(file) as file_1:
        data = file_1.read()
        print(data)


def main():
    """This function calls a function"""
    filename = '1log.txt'
    reading_file(filename)


if __name__ == '__main__':
    main()
