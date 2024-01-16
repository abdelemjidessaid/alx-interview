#!/usr/bin/python3
"""
    Module of a functiont that solves the minimum operations
"""


def minOperations(n) -> int:
    """
        Function that returns the minimum operations
        required to solve the copy paste
    """
    if not n or not isinstance(n, int) or n <= 1:
        return 0

    operations = 0
    factor = 2

    while factor * factor <= n:
        if n % factor == 0:
            n //= factor
            operations += factor
        else:
            factor += 1

    if n > 1:
        operations += n

    return operations
