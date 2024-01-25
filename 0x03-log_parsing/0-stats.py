#!/usr/bin/python3
"""
    Module contains a solution program of an Algorithm
"""
import sys
import re


codes = {
    '200': 0,
    '301': 0,
    '400': 0,
    '401': 0,
    '403': 0,
    '404': 0,
    '405': 0,
    '500': 0
}
file_size = 0
count = 0


def printResult():
    """
        Function that prints the result of calculation after
        10 lines or after keyboard interruption
    """
    # print the File size
    print(f'File size: {file_size}')
    # sort status codes
    sorted_keys = sorted(codes.keys())
    # print all keys and values of status codes except that has 0 in its value
    for key in sorted_keys:
        value = codes[key]
        if value:
            print(f'{key}: {value}')


try:
    for line in sys.stdin:
        # RegEx pattern to verify the input line instruction
        pattern = (
            r'(\d+\.\d+\.\d+\.\d+)' +
            r' - (\[\d+-\d+-\d+ \d+\:\d+\:\d+\.\d+\])' +
            r' (\"GET \/projects\/260 HTTP\/1.1\") (\d+) (\d+)')
        # result of the RegEx
        result = re.findall(pattern, line)
        # if RegEx result not None extract the Status code and File size
        if result:
            # get just status and file size from input Line
            status = result[0][3]
            size = result[0][4]
            # increment the number of status code and file size
            codes[status] += 1
            file_size += int(size)
        # increase the count var every iteration
        count += 1
        # if count is equal to 10 print the result of summation
        if count == 10:
            printResult()
            count = 0
except KeyboardInterrupt:
    pass
finally:
    printResult()
