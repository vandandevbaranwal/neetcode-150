# Pattern: Sliding Window — expand right until valid, shrink left to minimize
# Trigger: "minimum window containing all chars" = variable window = track have/need counts

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""

        countT, window = {}, {}

        # frequency of each character needed from t
        for c in t:
            countT[c] = 1 + countT.get(c, 0)

        have, need = 0, len(countT)   # have = chars satisfied, need = total unique chars in t
        res, resLen = [-1, -1], float("infinity")
        l = 0

        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0)

            # check if this char satisfies a requirement
            if c in countT and window[c] == countT[c]:
                have += 1

            # window is valid — try shrinking from left to minimize
            while have == need:
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = r - l + 1

                # shrink window from left
                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1   # lost a satisfied requirement
                l += 1

        l, r = res
        return s[l:r + 1] if resLen != float("infinity") else ""