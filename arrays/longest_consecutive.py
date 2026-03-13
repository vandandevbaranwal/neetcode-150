# Pattern: HashMap — track sequence boundaries, expand from edges in O(n)
# Trigger: "longest consecutive" = no sorting allowed = need O(n) = HashMap with boundary tracking

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        mp = defaultdict(int)
        res = 0
        for num in nums:
            if not mp[num]:
                mp[num] = mp[num - 1] + mp[num + 1] + 1
                mp[num - mp[num - 1]] = mp[num]
                mp[num + mp[num + 1]] = mp[num]
                res = max(res, mp[num])
        return res