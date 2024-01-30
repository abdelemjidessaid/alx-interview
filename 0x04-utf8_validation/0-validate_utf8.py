#!/usr/bin/python3
"""
    Module of UTF-8 validation
"""


def validUTF8(data) -> bool:
    """
        Function that validates UTF-8 from an array of data
    """
    if type(data) is not list:
        return False
    num_bytes = 0
    for byte in data:
        if type(byte) is not int:
            return False
        if byte & 0b11000000 == 0b10000000:
            if num_bytes == 0:
                return False
            num_bytes -= 1
        else:
            if num_bytes > 0:
                return False
            if byte & 0b11110000 == 0b11110000:
                num_bytes = 3
            elif byte & 0b11100000 == 0b11100000:
                num_bytes = 2
            elif byte & 0b11000000 == 0b11000000:
                num_bytes = 1
            elif byte & 0b10000000 == 0b10000000:
                return False

    return num_bytes == 0
