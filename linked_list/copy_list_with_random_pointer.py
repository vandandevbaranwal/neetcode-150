# Pattern: HashMap — map original nodes to their copies, then assign pointers
# Trigger: "deep copy with random pointers" = can't copy in one pass = map originals to copies first

"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        oldToCopy = {None: None}  # handles None next/random pointers elegantly

        # Pass 1 — create all copy nodes, map original → copy
        current = head
        while current:
            copy = Node(current.val)
            oldToCopy[current] = copy
            current = current.next

        # Pass 2 — assign next and random pointers using the map
        current = head
        while current:
            copy = oldToCopy[current]
            copy.next = oldToCopy[current.next]      # map original next to copy next
            copy.random = oldToCopy[current.random]  # map original random to copy random
            current = current.next

        return oldToCopy[head]