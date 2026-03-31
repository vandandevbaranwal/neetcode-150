# Pattern: Binary Search on Answer — search the solution space not the array
# Trigger: "minimum speed/capacity that satisfies condition" = binary search on the answer range

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)  # search space: slowest=1, fastest=max pile
        res = r

        while l <= r:
            k = (l + r) // 2  # try this eating speed
            totalTime = 0
            for p in piles:
                totalTime += math.ceil(float(p) / k)  # hours needed at speed k

            if totalTime <= h:
                res = k        # valid speed — try slower (minimize)
                r = k - 1
            else:
                l = k + 1      # too slow — try faster
        return res