"""Different functions that copy file content to another file"""


def copy_content(file1, file2):
    """Copying the complete file content to another"""
    with open(file1) as file_1:
        with open(file2, "w") as file_2:
            for line in file_1:
                file_2.write(line)


def copy_to_upper(file1, file2):
    """Copying the content of a file after converting to uppercase"""
    with open(file1) as file_1:
        with open(file2, "w") as file_2:
            for line in file_1:
                line1 = line.upper()
                file_2.write(line1)


def toggling_data(file1, file2):
    """Copying of the toggling data to another file"""
    with open(file1) as file_1:
        with open(file2, "w") as file_2:
            i = 1
            while 1:
                data = file_1.read(1)
                length = len(data)
                if data.islower():
                    data1 = data.upper()
                else:
                    data1 = data.lower()
                file_2.write(data1)

                i = i + 1
                if length < 1:
                    break


def substring_copy(file1, file2):
    """Copying all the lines which does not contain the sub string"""
    with open(file1) as file_1:
        with open(file2, "w") as file_2:
            sub = 'Hello'
            for line in file_1:
                if sub not in line:
                    file_2.write(line)


def space_copy(file1, file2):
    """Copying all the lines except the empty lines"""
    with open(file1) as file_1:
        with open(file2, "w") as file_2:
            for line in file_1:
                if line != '\n':
                    file_2.write(line)


def main():
    """This function contains the functions that are being called to do some task"""
    filename1 = '1log'
    filename2 = 'outputFile'
    copy_content(filename1, filename2)
    copy_to_upper(filename1, filename2)
    toggling_data(filename1, filename2)
    substring_copy(filename1, filename2)
    space_copy(filename1, filename2)


if __name__ == '__main__':
    main()
