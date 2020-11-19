def map_two_lists(list_1, list_2):
    return dict(zip(list_1, list_2))


def main():
    list_1 = [1, 2, 3, 4, 5, 6, 7]
    list_2 = ['one', 'two', 'three', 'four', 'five', 'six', 'seven']
    rval = map_two_lists(list_1, list_2)
    print(rval)


if __name__ == '__main__':
    main()
