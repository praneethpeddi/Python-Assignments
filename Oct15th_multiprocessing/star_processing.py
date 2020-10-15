"""This program executes a multiprocess of star type"""


import time
import multiprocessing
import os

def fun1():
    while True:
        print (f'In function1 : pid : {os.getpid()}, ppid : {os.getppid()}')
        time.sleep(2)
    return

def fun2():
    while(True):
        print (f'In function2 : pid : {os.getpid()}, ppid : {os.getppid()}')
        time.sleep(2)
    return

def fun3():
    while(True):
        print (f'In function3 : pid : {os.getpid()}, ppid : {os.getppid()}')
        time.sleep(2)
    return
	
def fun4():
    while(True):
        print (f'In function4 : pid : {os.getpid()}, ppid : {os.getppid()}')
        time.sleep(2)
    return
	
def fun5():
    while(True):
        print (f'In function5 : pid : {os.getpid()}, ppid : {os.getppid()}')
        time.sleep(2)
    return
	
def fun6():
    while(True):
        print (f'In function6 : pid : {os.getpid()}, ppid : {os.getppid()}')
        time.sleep(2)
    return
	
def fun7():
    while(True):
        print (f'In function7 : pid : {os.getpid()}, ppid : {os.getppid()}')
        time.sleep(2)
    return
	
def fun8():
    while(True):
        print (f'In function8 : pid : {os.getpid()}, ppid : {os.getppid()}')
        time.sleep(2)
    return
	
def fun9():
    while(True):
        print (f'In function9 : pid : {os.getpid()}, ppid : {os.getppid()}')
        time.sleep(2)
    return

def fun10():
    while(True):
        print (f'In function10 : pid : {os.getpid()}, ppid : {os.getppid()}')
        time.sleep(2)
    return
	
	
if __name__ == '__main__':
	print(f'Parent Process : pid : {os.getpid()}, ppid : {os.getppid()}')
	#for i in range(0, 10):
	p1 = multiprocessing.Process(target=fun1)
	p2 = multiprocessing.Process(target=fun2)
	p3 = multiprocessing.Process(target=fun3)
	p4 = multiprocessing.Process(target=fun4)
	p5 = multiprocessing.Process(target=fun5)
	p6 = multiprocessing.Process(target=fun6)
	p7 = multiprocessing.Process(target=fun7)
	p8 = multiprocessing.Process(target=fun8)
	p9 = multiprocessing.Process(target=fun9)
	p10 = multiprocessing.Process(target=fun10)
	p1.start()
	p2.start()
	p3.start()
	p4.start()
	p5.start()
	p6.start()
	p7.start()
	p8.start()
	p9.start()
	p10.start()