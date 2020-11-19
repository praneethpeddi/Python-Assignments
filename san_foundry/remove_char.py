def remove_character(str_, n):
    list_ = list(str_)
    if n <= len(str_):
        for i in range(1, len(list_)):
            if i == n:
                list_.pop(i - 1)
        for j in list_:
            print(j, end='')
    else:
        print("list index out of range")


def main():
    str_ = 'praneeth'
    n = 7
    remove_character(str_, n)


if __name__ == '__main__':
    main()
