def multiply_values(dict_):
    vals = list(dict_.keys())
    mul = 1
    for i in vals:
        mul = mul * i
    return mul


def main():
    dict_ = {1: 'one', 2: 'two', 3: 'three', 4: 'four'}
    rval = multiply_values(dict_)
    print(rval)


if __name__ == '__main__':
    main()
