#!/usr/bin/python3
"""
n number of locked boxes in front of you. Each box is numbered sequentially 
from 0 to n - 1 and each box may contain keys to the other boxes.
a method that determines if all the boxes can be opened.
"""

def canUnlockAll(boxes):

    if (type(boxes) is not list):
        return False    # box not in the this will return fales 

    if (len(boxes) == 0):
        return False    # box length equal to null return 0

    keys = [0]
    for i in keys:      # boxs determined all will opend
        for j in boxes[i]:
            if j not in keys and j != i and j < len(boxes) and j != 0:
                keys.append(j)
    if len(keys) == len(boxes):
        return True
    else:
        return False
