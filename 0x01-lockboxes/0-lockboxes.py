#!/usr/bin/python3

"""
  Module that holds a python function of canUnlockAll
"""


def canUnlockAll(boxes):
    """
        Function that check a 2D Array if all arrays that holds can
        be visited using their contained indexes.
    """

    num_boxes = len(boxes)
    unlocked_boxes = [False] * num_boxes
    unlocked_boxes[0] = True
    stack = [0]

    while stack:
        curr_box = stack.pop()

        # Iterate through the keys in the current box
        for key in boxes[curr_box]:
            if key < num_boxes and not unlocked_boxes[key]:
                unlocked_boxes[key] = True
                stack.append(key)

    return all(unlocked_boxes)
