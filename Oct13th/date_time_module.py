"""Program to print the date and time in the readable format"""


def date_time_conversion(inputs1, inputs2, a, b, c, d):
    """function to print the data and time in readable format"""
    tdate_s, ttime_s = inputs1.split('T')
    date1 = tdate_s.split('-')
    yy1, mm1, dd1 = int(date1[0]), int(date1[1]), int(date1[2])

    tdate_e, ttime_e = inputs2.split('T')
    date2 = tdate_e.split('-')
    yy2, mm2, dd2 = int(date2[0]), int(date2[1]), int(date2[2])

    if yy2 <= yy1:
        yy = yy1 - yy2
    else:
        yy = yy2 - yy1

    if mm2 <= mm1:
        mm = mm1 - mm2
    else:
        mm = mm2 - mm1

    if dd2 <= dd1:
        dd = dd1 - dd2
    else:
        dd = dd2 - dd1

    print(f'Difference in years: {yy}')
    print(f'Difference in months: {mm}')
    print(f'Difference in days: {dd}')

    time1 = ttime_s.split(':')
    time_in_sec1 = time1[2].split('.')
    hh1, min1 = int(time1[0]), int(time1[1])
    sec1 = int(time_in_sec1[0])

    time2 = ttime_e.split(':')
    time_in_sec2 = time2[2].split('.')
    hh2, min2 = int(time2[0]), int(time2[1])
    sec2 = int(time_in_sec2[0])

    if hh2 <= hh1:
        hh = hh1 - hh2
    else:
        hh = hh2 - hh1

    if min2 <= min1:
        min_s = min1 - min2
    else:
        min_s = min2 - min1

    if sec2 <= sec1:
        sec = sec1 - sec2
    else:
        sec = sec2 - sec1

    print(f'Difference in hours: {hh}')
    print(f'Difference in minutes: {min_s}')
    print(f'Difference in seconds: {sec}')

    diff_in_years = str(int(yy)) + 'years'
    diff_in_months = str(int(mm)) + 'months'
    diff_in_days = str(int(dd)) + 'days'
    diff_in_hours = str(int(hh)) + 'hours'
    diff_in_minutes = str(int(min_s)) + 'minutes'
    diff_in_seconds = str(int(sec)) + 'seconds'

    print(f'Difference between the start date and the end date is {yy} years, {mm} months, {dd} days, ' 
          f'{hh} hours, {min_s} minutes, {sec} seconds')

    return diff_in_years, diff_in_months, diff_in_days, diff_in_hours, diff_in_minutes, diff_in_seconds


def main():
    """this function calls the function 'date_time_conversion'"""
    str_start_date = '2018-12-30T09:37:56.000001Z'
    str_end_date = '2020-07-12T07:56:43.000001Z'
    a, b, c, d, e, f = date_time_conversion(str_start_date, str_end_date, 0, 0, 0, 0)


if __name__ == '__main__':
    main()
