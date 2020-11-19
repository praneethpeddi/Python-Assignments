def merge_and_sort(list_1, list_2):
    list_1.extend(list_2)
    list_1.sort()
    return list_1


def main():
    list_1 = [2, 4, 5, 8, 10, 9, 40, 78, 0, 1]
    list_2 = [4, 6, 6, 6, 6, 8, 0]
    sorted_list = merge_and_sort(list_1, list_2)
    print(f"Sorted list after merging two lists : {sorted_list}")


if __name__ == '__main__':
    main()
