def count_vowel(str_, vowel):
    count = 0
    for i in str_:
        if i in vowel:
            count += 1
    return count


def main():
    vowel = 'aeiou'
    str_ = 'Hello world'
    total_count = count_vowel(str_, vowel)
    print(total_count)


if __name__ == '__main__':
    main()