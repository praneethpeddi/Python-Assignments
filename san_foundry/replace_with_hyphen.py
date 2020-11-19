def replace_space_with_hyphen(str_):
    new_str = str_.replace(' ', '-')
    return new_str


def main():
    str_ = 'san foundr y  hyphen  python'
    output = replace_space_with_hyphen(str_)
    print(output)


if __name__ == '__main__':
    main()
