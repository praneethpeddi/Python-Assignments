def largest_string(str_1, str_2):
    count_str1 = 0
    count_str2 = 0
    for i in str_1:
        count_str1 += 1
    for j in str_2:
        count_str2 += 1
    if count_str1 > count_str2:
        print(f"{str_1} is larger")
    else:
        print(f"{str_2} is larger")


def main():
    str_1 = 'san foundry'
    str_2 = 'foundrrrrrrrrrrrrry'
    largest_string(str_1, str_2)


if __name__ == '__main__':
    main()
