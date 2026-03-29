# Pattern: Binary Search — eliminate half the search space each iteration
# Trigger: "sorted array + find target" = binary search = O(log n) instead of O(n)

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + r) // 2      # middle index
            if nums[m] > target:
                r = m - 1         # target in left half
            elif nums[m] < target:
                l = m + 1         # target in right half
            else:
                return m          # found!
        return -1                 # not found
    