def lower_case_count(str_):
    count_lower = 0
    count_upper = 0
    for i in str_:
        if i.islower():
            count_lower += 1
        elif i.isupper():
            count_upper += 1
    return count_lower, count_upper


def main():
    str_ = 'saSAP'
    count_lower, count_upper = lower_case_count(str_)
    print(f"lowercase count {count_lower}")
    print(f"uppercase count {count_upper}")


if __name__ == '__main__':
    main()
