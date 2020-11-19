def no_of_words_char(str_):
    words_count = len(str_.split(' '))
    chars_count = len(list(str_))
    return words_count, chars_count


def main():
    str_ = 'python is a language'
    words, chars = no_of_words_char(str_)
    print(words)
    print(chars)


if __name__ == '__main__':
    main()