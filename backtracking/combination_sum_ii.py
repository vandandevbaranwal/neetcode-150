# Pattern: Backtracking + Frequency Counting
# Trigger: "find unique combinations" + each number can be used at most once

class Solution:
    def combinationSum2(self, nums, target):
        self.res = []

        # value -> available count
        self.count = defaultdict(int)

        cur = []
        uniqueNums = []

        # build frequency map
        for num in nums:
            if self.count[num] == 0:
                uniqueNums.append(num)
            self.count[num] += 1

        self.backtrack(uniqueNums, target, cur, 0)

        return self.res

    def backtrack(self, nums, target, cur, i):

        # valid combination found
        if target == 0:
            self.res.append(cur.copy())
            return

        # invalid path
        if target < 0 or i >= len(nums):
            return

        # choice 1: take current number
        if self.count[nums[i]] > 0:
            cur.append(nums[i])
            self.count[nums[i]] -= 1

            self.backtrack(nums, target - nums[i], cur, i)

            # undo
            self.count[nums[i]] += 1
            cur.pop()

        # choice 2: skip current number entirely
        self.backtrack(nums, target, cur, i + 1)