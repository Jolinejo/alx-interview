#!/usr/bin/python3
"""
lockboxes
"""


def canUnlockAll(boxes):
    """
    checks if all boxes can be opened
    """
    queue = []
    uniq = set()
    uniq.add(0)
    for i in boxes[0]:
        if i not in uniq and i < len(boxes):
            uniq.add(i)
            queue.append(i)

    while len(queue):
        for i in boxes[queue[0]]:
            if i not in uniq and i < len(boxes):
                uniq.add(i)
                queue.append(i)
        queue.pop(0)
    if len(uniq) == len(boxes):
        return True
    return False
