# Pattern: Sliding Window — expand right, shrink left when duplicate found
# Trigger: "longest substring without repeating" = maintain valid window = sliding window + hashmap

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mp = {}   # stores most recent index of each character
        l = 0     # left pointer of window
        res = 0   # longest valid window seen so far

        for r in range(len(s)):
            if s[r] in mp:
                # duplicate found — jump left pointer past the previous occurrence
                # max() ensures left pointer never moves backwards
                l = max(mp[s[r]] + 1, l)
            mp[s[r]] = r          # update most recent index of this character
            res = max(res, r - l + 1)  # update longest window
        return res