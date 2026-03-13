# Pattern: Sorting — anagrams have identical sorted characters
# Trigger: "anagram" = same characters different order = sort both and compare

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)