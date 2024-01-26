#!/usr/bin/python3
"""
    Module contains a solution program of an Algorithm
"""
import sys
import re


# RegEx pattern to verify the input line instruction
pattern = (
    r'(\d+\.\d+\.\d+\.\d+)'
    r' - (\[\d+-\d+-\d+ \d+\:\d+\:\d+\.\d+\])'
    r' (\"GET \/projects\/260 HTTP\/1.1\") (\d+) (\d+)')
# dictionary Keys are sorted
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
file_size, count = 0, 0


def printResult() -> None:
    """
        Function that prints the result of calculation after
        10 lines or after keyboard interruption
    """
    # print the File size
    print('File size: {:d}'.format(file_size))
    # print all keys and values of status codes except that has 0 in its value
    for key in codes.keys():
        value = codes[key]
        if value:
            print('{}: {:d}'.format(key, value))


def convertInt(num: str) -> int:
    """
        Function that converts a string to integer
    """
    try:
        integer = int(num)
        return integer
    except TypeError:
        return 0


try:
    for line in sys.stdin:
        # increase the count var every iteration
        count += 1
        # result of the RegEx
        result = re.findall(pattern, line)
        # if RegEx result not None extract the Status code and File size
        if result:
            # get just status and file size from input Line
            status = result[0][3]
            size = result[0][4]
            # increment the number of status code and file size
            if status in codes:
                codes[status] += 1
            file_size += convertInt(size)
        # if count is equal to 10 print the result of summation
        if count == 10:
            printResult()
            count = 0
    printResult()
except KeyboardInterrupt:
    printResult()
    raise
