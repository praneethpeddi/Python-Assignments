import os
from pathlib import Path


def rename_of_file(old, new):
    try:
    	os.rename(old, new)
    except FileNotFoundError as err:
        print(err)

   
def get_file_name(input_file):
    with open(input_file,'r') as f_open:
    	data = f_open.readlines()
    	print(data)
    	for filename in data:
    	   old, new = filename.split(',')
    	   if (old != new):
    	       rename_of_file(old.strip(), new.strip())
    return
       
def main():
    input_file = 'data.txt'
    get_file_name(input_file)

if __name__ == '__main__':
    main()

