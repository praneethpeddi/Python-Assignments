import time
import multiprocessing


def print_hai():
    while True:
        print("P1: Hai")
        time.sleep(1)


def print_hello():
    while True:
        print("P2 : Hello")
        time.sleep(1)


if __name__ == '__main__':
    process1 = multiprocessing.Process(target=print_hai)
    process2 = multiprocessing.Process(target=print_hello)
    process1.start()
    process2.start()

