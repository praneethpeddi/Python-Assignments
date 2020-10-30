def ListOfString(file):
    with open(file) as f:
        data = f.readlines()
        print(data)


Filename = '1log'
ListOfString(Filename)
