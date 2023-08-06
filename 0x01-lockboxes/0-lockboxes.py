#!/usr/bin/python3
'''
Module 0-lockboxes
Function to determine if all lock box can be opened
'''


def canUnlockAll(boxes):
    '''
    check if index of list is contained in list of lists
    '''
    unlocked = [0]
    for box_id, box in enumerate(boxes):
        if not box:
            continue
        for key in box:
            if key < len(boxes) and key not in unlocked and key != box_id:
                unlocked.append(key)
    if len(unlocked) == len(boxes):
        return True
    return False
