"""Program to update the config file"""


filename = 'dhcpd-conf'


def get_data_by_file_name(input_file):
    start_pos = 'host '
    end_pos = '}'
    new_data = ''
    file_data = open('dhcpd.conf', 'r')
    hardware_ethernet = []
    while True:
        line = file_data.readline()
        if line.startswith(start_pos):
            new_data = line
        else:
            new_data += line
            if line.find('hardware ethernet') != -1:
                line = line.lstrip()
                line2 = line.split(' ')
                hardware_id = line2[-1].rstrip(';\n')
                hardware_ethernet.append(hardware_id)
        if line.endswith(end_pos):
            pass
        if not line:
            file_data.close()
            return new_data, hardware_ethernet


def reading_csv_file():
    file_data = open('fixed-ip-list.csv', 'r')
    csv_data = {}
    while True:
        line = file_data.readline()
        name = line.split(',')
        if len(name) > 1:
            csv_data[name[0]] = name[1].rstrip('\n')
        if not line:
            return csv_data


def get_IP(last_conf):
    for line in last_conf.split('\n'):
        if line.find('fixed-address') != -1:
            line = line.lstrip()
            line = line.split()
            last_digit = line[1].split('.')[-1].rstrip(';')
            return int(last_digit)


def updated_dhcpd_data(last_digit, csv_data, hardware_list):
    updt_data = ''
    for name, hw_id in csv_data.items():
        if hw_id not in hardware_list:
            last_digit += 1
            print()
            print('192.168.1.' + str(last_digit))
            updt_data += 'host ' + name + ' {\n'
            updt_data += ' ' * 8 + 'hardware ethernet ' + hw_id + ';\n'
            updt_data += ' ' * 8 + 'fixed-address ' + '192.168.1.' + str(last_digit) + ';\n'
            updt_data += ' ' * 8 + 'option routers 192.168.1.1;\n}\n\n'
    return updt_data


def write_dhcpd_conf(updt_data):
    data = open('dhcpd.conf', 'a')
    data.write(updt_data)
    data.close()


def main():
    last_conf, hardware_list = get_data_by_file_name(filename)
    print(last_conf, hardware_list)
    last_digit = get_IP(last_conf)
    print(last_digit)
    csv_data = reading_csv_file()
    print(csv_data)
    updt_data = updated_dhcpd_data(last_digit, csv_data, hardware_list)
    print(updt_data)
    write_dhcpd_conf(updt_data)


if __name__ == '__main__':
    main()
