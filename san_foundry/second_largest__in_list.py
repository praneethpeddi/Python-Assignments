def second_largest(list_):
    list_.sort()
    unique_list = list(set(list_))
    sec_max = unique_list[-2]
    return sec_max


def main():
    list_ = [2, 20, 5, 6, 10, 9, 6, 89, 89, 56, 56]
    sec_max = second_largest(list_)
    print(f"second largest element in the list {list_} : {sec_max}")


if __name__ == '__main__':
    main()