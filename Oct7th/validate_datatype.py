"""Program to validate the data types"""


def datatype_validation(inputs):
    if isinstance(inputs, int):
        pass
    elif isinstance(inputs, str):
        pass
    elif isinstance(inputs, float):
        pass
    return type(inputs)


def main():
    """Function that passes the different data types"""
    inputting = [(5, int),  (6, int), ('string', str), (5.7, float)]
    for i in inputting:
        outputs = datatype_validation(i[0])
        if outputs == i[1]:
            print(f'validation of type {i[0]} is {i[1]} : validation success')
        else:
            print(f'validation of type {i[0]} is not {i[1]} : validation failed')


if __name__ == "__main__":
    main()
