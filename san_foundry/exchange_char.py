def exchange(str_):
    first_char = str_[:1]
    last_char = str_[-1:]
    char_ = str_[1:-1]
    updated_str = last_char + char_ + first_char
    return updated_str


def main():
    str_ = 'exchangechar'
    str_update = exchange(str_)
    print(str_update)


if __name__ == '__main__':
    main()