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
    print(f'File size: {file_size}')
    sorted_keys = sorted(codes.keys())
    for key in sorted_keys:
        value = codes[key]
        if value:
            print(f'{key}: {value}')


try:
    for line in sys.stdin:
        pattern = (
            r'(\d+\.\d+\.\d+\.\d+)' +
            r' - (\[\d+-\d+-\d+ \d+\:\d+\:\d+\.\d+\])' +
            r' (\"GET \/projects\/260 HTTP\/1.1\") (\d+) (\d+)')
        result = re.findall(pattern, line)
        if result:
            status = result[0][3]
            size = result[0][4]
            # increment the number of status code and file size
            codes[status] += 1
            file_size += int(size)
        count += 1
        if count == 10:
            printResult()
            count = 0
except Exception:
    pass
finally:
    printResult()
