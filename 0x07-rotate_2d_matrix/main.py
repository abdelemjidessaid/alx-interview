#!/usr/bin/python3
"""
Test 0x07 - Rotate 2D Matrix
"""
rotate_2d_matrix = __import__('0-rotate_2d_matrix').rotate_2d_matrix

if __name__ == "__main__":
    matrix = [['1', '2', '3', 'A'],
              ['4', '5', '6', 'B'],
              ['7', '8', '9', 'C'],
              ['D', 'E', 'F', 'G']]

    n = len(matrix)
    print('-- Before --')
    for i in range(n):
        print(matrix[i])

    rotate_2d_matrix(matrix)

    print('-- After --')
    for i in range(n):
        print(matrix[i])
