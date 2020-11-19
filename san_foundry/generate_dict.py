def generate_dictionary(n):
    dict_ = {}
    for i in range(1, n+1):
        dict_[i] = i*i
    print(dict_)


def main():
    n = 20
    generate_dictionary(n)


if __name__ == '__main__':
    main()
