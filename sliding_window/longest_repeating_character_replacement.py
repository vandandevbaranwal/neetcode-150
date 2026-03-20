# Pattern: Sliding Window — expand right, shrink left when window becomes invalid
# Trigger: "replace k characters" = maintain valid window = window size - max frequency <= k

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}   # frequency of each character in current window
        res = 0
        l = 0
        maxf = 0     # frequency of most common character in window

        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            maxf = max(maxf, count[s[r]])

            # window invalid when replacements needed > k
            # replacements needed = window size - most frequent char count
            while (r - l + 1) - maxf > k:
                count[s[l]] -= 1   # shrink window from left
                l += 1
            res = max(res, r - l + 1)
        return res