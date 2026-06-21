# Pattern: Backtracking (Choose → Explore → Undo)
# Trigger: "find all combinations" + can reuse elements = backtracking

class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        # sort to enable pruning
        nums.sort()

        def dfs(i, cur, total):

            # valid combination found
            if total == target:
                res.append(cur.copy())
                return

            for j in range(i, len(nums)):

                # pruning: no need to explore further
                if total + nums[j] > target:
                    return

                # choose
                cur.append(nums[j])

                # explore (reuse allowed, so pass j)
                dfs(j, cur, total + nums[j])

                # undo
                cur.pop()

        dfs(0, [], 0)

        return res