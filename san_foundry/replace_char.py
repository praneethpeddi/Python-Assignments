def replace_char_in_str(str_):
    new_str = str_.replace('a', '$')
    return new_str


def main():
    str_ = 'san foundry'
    output = replace_char_in_str(str_)
    print(output)


if __name__ == '__main__':
    main()
