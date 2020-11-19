def concatenate_dictionary(dict_1, dict_2):
    dict_1.update(dict_2)
    return dict_1


def main():
    dict_1 = {1: 'one', 2: 'two', 3: 'three'}
    dict_2 = {4: 'four', 5: 'five'}
    dict_ = concatenate_dictionary(dict_1, dict_2)
    print(dict_)


if __name__ == '__main__':
    main()
