"""Doc Stings"""


def main():
    """Passes the list of words to the function substring_search"""
    # print(main.__doc__)
    tolist = ['Hello world', "Bye World", "I am in this WORLD"]
    substring_search(tolist)


def substring_search(inputs):
    """Takes the argument from the function main"""
    # print(substring_search.__doc__)
    sub_str = 'world'
    count = 0
    for line in inputs:
        if sub_str in line.lower():
            count = count + 1
    print(f"{sub_str} is present in the given list for {count} number of times")


if __name__ == '__main__':
    main()
