# Pattern: Backtracking + Palindrome Checking
# Trigger: "partition string" + every substring must satisfy a condition = backtracking

class Solution:

    def partition(self, s: str) -> List[List[str]]:
        res = []
        part = []

        def dfs(i):

            # reached end of string → valid partition found
            if i >= len(s):
                res.append(part.copy())
                return

            # try every possible substring starting at i
            for j in range(i, len(s)):

                # choose only if substring is a palindrome
                if self.isPali(s, i, j):

                    # choose
                    part.append(s[i:j + 1])

                    # explore remaining string
                    dfs(j + 1)

                    # undo
                    part.pop()

        dfs(0)
        return res

    def isPali(self, s, l, r):

        # check if substring s[l:r] is a palindrome
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1

        return True