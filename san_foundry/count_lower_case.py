def lower_case_count(str_):
    count = 0
    for i in str_:
        if i.islower():
            count += 1
    return count


def main():
    str_ = 'sanSFoundry'
    count_lower = lower_case_count(str_)
    print(count_lower)


if __name__ == '__main__':
    main()
