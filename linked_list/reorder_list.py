# Pattern: Fast & Slow + Reverse + Merge — three steps to reorder in place
# Trigger: "reorder list L0→Ln→L1→Ln-1" = find middle, reverse second half, merge both halves

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        # Step 1 — find middle using fast & slow pointers
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Step 2 — reverse the second half of the list
        second = slow.next
        prev = slow.next = None    # cut list in half
        while second:
            tmp = second.next
            second.next = prev     # reverse pointer
            prev = second
            second = tmp

        # Step 3 — merge first half and reversed second half alternately
        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second    # insert second half node
            second.next = tmp1     # connect back to first half
            first, second = tmp1, tmp2