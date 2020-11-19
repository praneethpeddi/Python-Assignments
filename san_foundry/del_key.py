def delete_key(dict_, key):
    k = list(dict_.keys())
    if key in k:
        del dict_[key]
    return dict_


def main():
    dict_ = {1: 'one', 2: 'two', 3: 'three'}
    key = 1
    rval = delete_key(dict_, key)
    print(rval)


if __name__ == '__main__':
    main()
