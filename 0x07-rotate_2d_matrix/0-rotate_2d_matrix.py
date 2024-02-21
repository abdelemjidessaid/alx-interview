#!/usr/bin/python3
""" Module of rotating the 2D matrix """


def rotate_2d_matrix(matrix):
    """ Function that rotate a 2D matrix 90 degree """
    n = len(matrix)
    for i in range(int(n / 2)):
        for j in range(i, n - i - 1):
            # save top values
            tmp = matrix[i][j]
            # move left values to top row
            matrix[i][j] = matrix[n - j - 1][i]
            # move bottom values to left column
            matrix[n - j - 1][i] = matrix[n - i - 1][n - j - 1]
            # move right values to bottom row
            matrix[n - i - 1][n - j - 1] = matrix[j][n - i - 1]
            # set the top values in right column
            matrix[j][n - i - 1] = tmp
