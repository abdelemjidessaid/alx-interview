#!/usr/bin/python3
"""
    Module of UTF-8 validation
"""


def validUTF8(data) -> bool:
    """
        Function that validates UTF-8 from an array of data
    """
    if type(data) is list and data:
        if len(data) <= 64:
            for value in data:
                if not (type(value) is int and (value >= 0 and value <= 128)):
                    return False
            return True
    return False
