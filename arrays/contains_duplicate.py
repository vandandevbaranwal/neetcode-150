# Pattern: HashSet — store seen elements, check membership in O(1)
# Trigger: "contains duplicate" = need to track what we've seen before

class Solution:
    def containsDuplicate(self, nums):
        seen = set()           # O(n) space — trades memory for O(1) lookup
        for num in nums:
            if num in seen:    # duplicate found — set already has this number
                return True
            seen.add(num)      # first time seeing this number, record it
        return False           # looped through all, no duplicates found