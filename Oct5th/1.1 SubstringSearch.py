def main():
    tolist = ['Hello world', "Bye World", "I am in this WORLD"]
    SubStringSearch(tolist)


def SubStringSearch(inputs):
    sub_str = 'world'
    count = 0
    for line in inputs:
        if sub_str in line.lower():
            count = count + 1
    print(sub_str + " is present in the given list for " + str(count) + " number of times")


if __name__ == '__main__':
    main()
