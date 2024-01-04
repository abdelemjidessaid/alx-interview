#!/usr/bin/python3

"""
    Function that make the Pascal Traingle with 2D list
"""


def pascal_triangle(n):
    """
        Function that make the Pascal Traingle with 2D list
    """

    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        row = [1]
        prev_row = triangle[i - 1]

        for j in range(1, i):
            row.append(prev_row[j - 1] + prev_row[j])

        row.append(1)
        triangle.append(row)

    return triangle
