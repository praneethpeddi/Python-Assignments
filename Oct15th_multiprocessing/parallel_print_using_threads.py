from threading import Thread
import time
import os


def fun1():
	while 1:
		print(f'Hai : my pid : {os.getpid()}, my parent pid : {os.getppid()}')
		time.sleep(2)
	return
	
def fun2():
	while 1:
		print(f'Hello : my pid : {os.getpid()}, my parent pid : {os.getppid()}')
		time.sleep(2)
	return


if __name__ == '__main__':
	print(f'parent process : my pid : {os.getpid()}, my parent pid : {os.getppid()}')
	t1 = Thread(target=fun1)
	t2 = Thread(target=fun2)
	t1.start()
	t2.start()
