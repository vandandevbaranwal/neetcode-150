# Pattern: Two Pointers — greedy, always move the shorter side inward
# Trigger: "container/area between two lines" = maximize width * height = two pointers from ends

class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        res = 0
        while l < r:
            # area = shorter height * width between pointers
            area = min(heights[l], heights[r]) * (r - l)
            res = max(res, area)
            # move the shorter side — moving taller side can never increase area
            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1
        return res