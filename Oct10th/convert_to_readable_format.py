"""This program convert a elapsed time to readable date and time"""


from datetime import datetime


def convert_to_str():
    """This function prints the difference between two dates"""
    str_time = datetime.strptime('2018-09-17T12:57:29.000001Z', '%Y-%m-%dT%H:%M:%S.%fZ')
    # print(str_time)
    end_time = datetime.strptime('2020-07-17T19:57:29.000001Z', '%Y-%m-%dT%H:%M:%S.%fZ')
    # print(end_time)
    diff = end_time - str_time
    print(f'The difference between {str_time} and {end_time} is {diff}')


def main():
    convert_to_str()


if __name__ == '__main__':
    main()
