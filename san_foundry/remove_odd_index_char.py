def remove_odd_char(str_):
    lis = []
    list_str = list(str_)
    print(list_str)
    for i in range(len(list_str)):
        if i % 2 == 0:
            lis.append(str_[i])
    for i in lis:
        print(i, end='')


def main():
    str_ = 'sanfoundry'
    remove_odd_char(str_)


if __name__ == '__main__':
    main()
