# Pattern: Two Pointers (Gap Technique) — maintain n gap between pointers to find nth from end
# Trigger: "nth from end" = don't know length = two pointers with fixed gap = one pass solution

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)  # dummy handles edge case of removing head node
        left = dummy
        right = head

        # advance right pointer n steps ahead — creates gap of n between pointers
        while n > 0:
            right = right.next
            n -= 1

        # move both together until right hits end
        # left is now just before the node to remove
        while right:
            left = left.next
            right = right.next

        # remove the nth node from end
        left.next = left.next.next

        return dummy.next