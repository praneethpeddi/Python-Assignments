def length_of_string(str_):
    count = 0
    for i in list(str_):
        count += 1
    return count


def main():
    str_ = 'python is a language'
    output = length_of_string(str_)
    print(output)


if __name__ == '__main__':
    main()