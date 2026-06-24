# Pattern: Backtracking + Duplicate Skipping
# Trigger: "generate all subsets" + duplicates exist = skip duplicate branches

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()  # bring duplicates together

        res = []

        def backtrack(i, subset):

            # every state is a valid subset
            res.append(subset[:])

            for j in range(i, len(nums)):

                # skip duplicate branches at same recursion level
                if j > i and nums[j] == nums[j - 1]:
                    continue

                # choose
                subset.append(nums[j])

                # explore
                backtrack(j + 1, subset)

                # undo
                subset.pop()

        backtrack(0, [])

        return res