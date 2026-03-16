# Pattern: Two Pointers + Sorting — fix one element, use two pointers for the remaining pair
# Trigger: "three sum = zero" = reduce to two sum by fixing first element + skip duplicates

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()  # sort first — enables two pointer + duplicate skipping
        for i, a in enumerate(nums):
            # skip duplicate values for first element
            if i > 0 and a == nums[i - 1]:
                continue
            l, r = i + 1, len(nums) - 1
            while l < r:
                threeSum = a + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1       # sum too big — move right pointer left
                elif threeSum < 0:
                    l += 1       # sum too small — move left pointer right
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    # skip duplicates for second element after finding a valid triplet
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        return res