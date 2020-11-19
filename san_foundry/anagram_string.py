def anagram_check(str_1, str_2):
    if sorted(str_2) == sorted(str_1):
        print("Strings are anagrams")
    else:
        print("Strings are not anagrams")


def main():
    str_1 = 'anagram'
    str_2 = 'nagaram'
    anagram_check(str_1, str_2)


if __name__ == '__main__':
    main()
