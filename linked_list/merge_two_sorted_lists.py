# Pattern: Dummy Node + Two Pointers — merge by comparing heads, advance the smaller one
# Trigger: "merge two sorted lists" = pick smaller head each time = dummy node for clean return

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        dummy = node = ListNode()  # dummy head — avoids edge case of empty result list

        while list1 and list2:
            if list1.val < list2.val:
                node.next = list1  # attach smaller node
                list1 = list1.next # advance list1 pointer
            else:
                node.next = list2  # attach smaller node
                list2 = list2.next # advance list2 pointer
            node = node.next       # advance result pointer

        # attach remaining nodes — one list is exhausted, other still has nodes
        node.next = list1 or list2

        return dummy.next          # skip dummy head, return actual result
    