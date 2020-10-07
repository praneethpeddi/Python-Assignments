"""Program to print the data Program to print the data """


def start_with_string(inputs):
    """Function prints the data where the line starts with the substring"""
    sub = 'Python'
    for line in inputs.split('\n'):
        if line.startswith(sub):
            print(line)


def main():
    """This function calls a function"""
    string = """Python is a programming language
    file is opened in write mode """
    start_with_string(string)


if __name__ == '__main__':
    main()
