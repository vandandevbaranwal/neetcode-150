# Pattern: Dummy Node + Carry — simulate addition digit by digit with carry
# Trigger: "add numbers stored in linked list" = process digit by digit = carry like normal addition

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()    # dummy head for clean result list
        current = dummy
        carry = 0             # carry from previous digit addition

        while l1 or l2 or carry:   # continue while nodes exist OR carry remains
            v1 = l1.val if l1 else 0   # handle lists of different lengths
            v2 = l2.val if l2 else 0

            val = v1 + v2 + carry      # sum including carry
            carry = val // 10          # carry for next digit
            val = val % 10             # actual digit to store

            current.next = ListNode(val)
            current = current.next

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next
    