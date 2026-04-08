# Pattern: Fast & Slow Pointers (Floyd's Algorithm) — two pointers at different speeds
# Trigger: "detect cycle" = can't use extra space = fast/slow pointers must meet if cycle exists

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next        # moves 1 step
            fast = fast.next.next   # moves 2 steps
            if slow == fast:        # they met — cycle exists
                return True

        return False                # fast reached end — no cycle