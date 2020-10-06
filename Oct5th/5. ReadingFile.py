def ReadingFile(file):
    with open(file) as f:
        data = f.read()
        print(data)


Filename = '1log'
ReadingFile(Filename)