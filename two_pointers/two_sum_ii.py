# Pattern: Two Pointers — use sorted property to move pointers intelligently
# Trigger: "sorted array + find pair" = two pointers from both ends, no extra space needed

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1
        while l < r:
            curSum = numbers[l] + numbers[r]
            if curSum > target:
                r -= 1      # sum too big — move right pointer left to decrease
            elif curSum < target:
                l += 1      # sum too small — move left pointer right to increase
            else:
                return [l + 1, r + 1]   # 1-indexed result
        return []