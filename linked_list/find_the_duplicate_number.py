# Pattern: Fast & Slow Pointers (Floyd's Cycle Detection) — treat array as linked list
# Trigger: "find duplicate without extra space" = array values as pointers = cycle detection

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        # Phase 1 — detect cycle (same as linked list cycle detection)
        # treat index as node, nums[index] as next pointer
        slow, fast = 0, 0
        while True:
            slow = nums[slow]           # move 1 step
            fast = nums[nums[fast]]     # move 2 steps
            if slow == fast:            # cycle detected
                break

        # Phase 2 — find cycle entry point = duplicate number
        # move one pointer from start, keep other at meeting point
        # they meet at the cycle entry = duplicate
        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow
            