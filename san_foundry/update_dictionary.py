def update_dict(dict_):
    dict_.update({4: 'four'})
    return dict_


def main():
    dict_ = {1: 'one', 2: 'two', 3: 'three'}
    updated_dictionary = update_dict(dict_)
    print(updated_dictionary)


if __name__ == '__main__':
    main()
