def StartWithSubStr(inputs):
    substr = 'Python'
    for line in inputs.split('\n'):
        if line.startswith(substr):
            print(line)


if __name__ == '__main__':
    string = """Python is a programming language 
    file is opened in write mode """
    StartWithSubStr(string)
