# Pattern: Two Pointers — shrink window from both ends, skip non-alphanumeric chars
# Trigger: "palindrome" = compare from both ends = two pointers moving toward center

class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        while l < r:
            # skip non-alphanumeric characters from left
            while l < r and not self.alphaNum(s[l]):
                l += 1
            # skip non-alphanumeric characters from right
            while r > l and not self.alphaNum(s[r]):
                r -= 1
            # mismatch found — not a palindrome
            if s[l].lower() != s[r].lower():
                return False
            l, r = l + 1, r - 1
        return True

    def alphaNum(self, c):
        # manual check using ASCII ranges — avoids importing re or using isalnum()
        return (ord('A') <= ord(c) <= ord('Z') or
                ord('a') <= ord(c) <= ord('z') or
                ord('0') <= ord(c) <= ord('9'))