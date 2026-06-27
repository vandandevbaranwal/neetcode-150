# Pattern: Backtracking (Decision Tree)
# Trigger: "generate all possible combinations" = choose one option at each position

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []

        # mapping of digit -> possible letters
        digitToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        def backtrack(i, curStr):

            # complete combination formed
            if len(curStr) == len(digits):
                res.append(curStr)
                return

            # try every letter mapped to current digit
            for c in digitToChar[digits[i]]:

                # choose + explore
                backtrack(i + 1, curStr + c)

        # edge case: empty input
        if digits:
            backtrack(0, "")

        return res