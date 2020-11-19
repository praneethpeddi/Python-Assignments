def check_for_key(dict_, key):
    k = list(dict_.keys())
    if key in k:
        return True
    else:
        return False


def main():
    dict_ = {1: 'one', 2: 'two', 3: 'three'}
    key = 1
    rval = check_for_key(dict_, key)
    print(rval)


if __name__ == '__main__':
    main()
