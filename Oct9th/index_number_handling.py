import sys


def index_error():
    """Checking for the index number of an element"""
    ele = [4, 5, 6, 8, 567]
    try:
        print(ele.index(67))
    except Exception as e:
        print(e)


def main():
    index_error()


if __name__ == '__main__':
    main()
