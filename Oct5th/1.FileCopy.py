def CopyContent(file1, file2):
    with open(file1) as f:
        with open(file2, "w") as f1:
            for line in f:
                f1.write(line)


def CopyContentToUpper(file1, file2):
    with open(file1) as f:
        with open(file2, "w") as f1:
            for line in f:
                line1 = line.upper()
                f1.write(line1)


def TogglingData(file1, file2):
    with open(file1) as f:
        with open(file2, "w") as f1:
            i = 1
            while 1:
                data = f.read(1)
                length = len(data)
                if data.islower():
                    data1 = data.upper()
                else:
                    data1 = data.lower()
                f1.write(data1)

                i = i + 1
                if length < 1:
                    break


def SubStringNotCopy(file1, file2):
    with open(file1) as f:
        with open(file2, "w") as f1:
            sub = 'Hello'
            for line in f:
                if sub not in line:
                    f1.write(line)


def SpaceNotCopy(file1, file2):
    with open(file1) as f:
        with open(file2, "w") as f1:
            for line in f:
                if line != '\n':
                    f1.write(line)


filename1 = '1log'
filename2 = 'outputFile'
CopyContent(filename1, filename2)
CopyContentToUpper(filename1, filename2)
TogglingData(filename1, filename2)
SubStringNotCopy(filename1, filename2)
SpaceNotCopy(filename1, filename2)
