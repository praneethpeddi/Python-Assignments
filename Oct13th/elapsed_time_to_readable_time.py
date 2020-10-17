"""This program imports a user defined module"""


from date_time_module import date_time_conversion


def main():
    """this function calls a function which is created in the user defined module"""
    date_time_conversion('2018-12-30T09:37:56.000001Z', '2020-07-12T07:56:43.000001Z', 0, 0, 0, 0)


if __name__ == '__main__':
    main()
