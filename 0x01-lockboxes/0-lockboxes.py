#!/usr/bin/python3

"""
  Module that holds a python function of canUnlockAll
"""


def canUnlockAll(boxes):
    """
        Function that check a 2D Array if all arrays that holds can
        be visited using their contained indexes.
    """

    if boxes is None or len(boxes) == 0:
        return False

    visited = [0]
    i = 0
    # visite all boxes mentioned
    while (i < len(boxes)):
        box = boxes[i]
        inc = True
        for j in box:
            if j in visited:
                continue
            else:
                visited.append(j)
                i = j
                inc = False
                break
        if inc:
            i += 1
    # check if all boxes visited and return True or False
    for i in range(len(boxes)):
        if i not in visited:
            return False
    return True
