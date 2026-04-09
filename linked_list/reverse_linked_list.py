# Pattern: Recursive Linked List — reverse by fixing pointers on the way back up
# Trigger: "reverse linked list" = change next pointers = recursion or iterative two pointer

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        newHead = head

        if head.next:
            # recurse all the way to the last node — that becomes new head
            newHead = self.reverseList(head.next)
            # on the way back up, make next node point back to current
            head.next.next = head

        head.next = None   # cut original forward pointer to avoid cycle
        return newHead