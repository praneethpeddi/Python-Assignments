def palindrome_check(str_):
    if str_[::-1] == str_:
        print(f"{str_} is palindrome")
    else:
        print(f"{str_} is not palindrome")


def main():
    str_ = 'madamater'
    palindrome_check(str_)


if __name__ == '__main__':
    main()
