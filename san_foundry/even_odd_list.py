def even_odd(list_):
    list_even = []
    list_odd = []
    for num in list_:
        if num % 2 == 0:
            list_even.append(num)
        else:
            list_odd.append(num)

    return list_even, list_odd


def main():
    list_ = []
    for ele in range(25):
        list_.append(ele)
    even, odd = even_odd(list_)
    print(f"list of even numbers    : {even}")
    print(f"list of odd numbers     : {odd}")
    even_no = list(filter(lambda x: (x % 2 == 0), list_))
    print(f"list of even numbers    : {even_no}")
    odd_no = list(filter(lambda y: (y % 2 != 0), list_))
    print(f"list of odd numbers     : {odd_no}")


if __name__ == '__main__':
    main()