#!/usr/bin/python3
'''
Module 0-lockboxes
Function to determine if all lock box can be opened
'''
from typing import List


def canUnlockAll(boxes: List[List]) -> bool:
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

# BFS approach
# from collections import deque
# from typing import List

# def canUnlockAll(boxes: List[List[int]]) -> bool:
#     n = len(boxes)
#     visited = [False] * n
#     visited[0] = True

#     queue = deque([0])

#     while queue:
#         current_box = queue.popleft()
#         for key in boxes[current_box]:
#             if not visited[key]:
#                 visited[key] = True
#                 queue.append(key)
#    return all(visited)
