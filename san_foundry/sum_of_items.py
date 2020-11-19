def sum_of_items_in_dict(dict_):
    return sum(list(dict_.keys()))


def main():
    dict_ = {1: 'one', 2: 'two', 3: 'three'}
    sum_val = sum_of_items_in_dict(dict_)
    print(sum_val)


if __name__ == '__main__':
    main()
