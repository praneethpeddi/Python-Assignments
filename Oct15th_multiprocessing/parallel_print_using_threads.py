import threading
from threading import Thread
from threading import current_thread
import time
import os


def fun1():
	while 1:
		print(f'Hai : my pid : {threading.get_ident()}')
		time.sleep(2)
	return


def fun2():
	while 1:
		print(f'Hello : my id : {threading.get_ident()}')
		time.sleep(2)
	return


if __name__ == '__main__':
	print(f'parent process : my id : {threading.get_ident()}, parent : {threading.current_thread()}')
	t1 = Thread(target=fun1)
	t2 = Thread(target=fun2)
	t1.start()
	t2.start()