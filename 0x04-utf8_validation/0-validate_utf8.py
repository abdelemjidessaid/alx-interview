#!/usr/bin/python3
"""
    Module of UTF-8 validation
"""


def validUTF8(data) -> bool:
    """
        Function that validates UTF-8 from an array of data
    """
    left_bytes = 0
    if type(data) is list and data:
        for value in data:
            if type(value) is int:
                if value >> 6 == 0b10:
                    if left_bytes == 0:
                        return False
                    left_bytes -= 1
                else:
                    if left_bytes > 0:
                        return False
                    if value >> 7 == 0b0:
                        left_bytes = 0
                    elif value >> 5 == 0b110:
                        left_bytes = 1
                    elif value >> 4 == 0b1110:
                        left_bytes = 2
                    elif value >> 3 == 0b11110:
                        left_bytes = 3
                    else:
                        return False
            else:
                return False
    else:
        return False
    return left_bytes == 0
