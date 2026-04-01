# Pattern: Binary Search — compare mid with right to determine which half is sorted
# Trigger: "rotated sorted array + find minimum" = modified binary search = eliminate sorted half

class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1

        while l < r:
            m = l + (r - l) // 2      # avoids integer overflow (good habit)
            if nums[m] < nums[r]:
                r = m                  # mid is in the sorted right half
                                       # minimum could be at mid or left of mid
            else:
                l = m + 1              # mid is in the unsorted left half
                                       # minimum must be to the right of mid
        return nums[l]                 # l == r, converged on minimum
    