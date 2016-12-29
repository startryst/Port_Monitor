#!/usr/bin/env python


# Environment requirement:
# 1. CentOS 6.8 with network tools 'nc' installed, due to different output of 'nc' in Mac, Mac has some problems
# 2. Python 2.6.6/2.7.10 interpreter
# chmod 755 for this file to run directly

import subprocess
from datetime import datetime


def get_ip_list(ip_file):
    ip_list = []
    for line in open(ip_file):
        line = line.strip('\n')
        ip_list.append(line.split(','))
    return ip_list


def nc_test(ip_list, result_file):
    for i in ip_list:
        output = subprocess.Popen(['nc', '-w', '2', '-z', i[0], i[1]], stdout=subprocess.PIPE).communicate()[0]
        if output == '':
            result = '|' + str(datetime.now()).ljust(30) + '|' + (i[0] + ':' + i[1]).ljust(20) + '|' + 'FAILED'.ljust(10)
            print result
            save_to_file(result, result_file)
        else:
            result = '|' + str(datetime.now()).ljust(30) + '|' + (i[0] + ':' + i[1]).ljust(20) + '|' + 'SUCCESS'.ljust(10)
            print result
            save_to_file(result, result_file)


def save_to_file(result, result_file):
    file_to_save = open(result_file, "a")
    file_to_save.write('\n' + result)
    file_to_save.close()


def main():
    ip_file = raw_input('Please enter the file name to monitor: ')
    result_file = raw_input('Please enter the fine name to save for the monitor result: ')
    while True:
        nc_test(get_ip_list(ip_file), result_file)

if __name__ == '__main__':
    main()


