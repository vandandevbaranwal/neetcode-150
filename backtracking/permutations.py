# Pattern: Backtracking + Visited Array
# Trigger: "generate all permutations" = choose one unused element at each position

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.res = []

        # track which numbers are already used in current permutation
        self.backtrack([], nums, [False] * len(nums))

        return self.res

    def backtrack(self, perm: List[int], nums: List[int], pick: List[bool]):

        # complete permutation formed
        if len(perm) == len(nums):
            self.res.append(perm[:])
            return

        for i in range(len(nums)):

            # skip already used elements
            if not pick[i]:

                # choose
                perm.append(nums[i])
                pick[i] = True

                # explore
                self.backtrack(perm, nums, pick)

                # undo (backtrack)
                perm.pop()
                pick[i] = False