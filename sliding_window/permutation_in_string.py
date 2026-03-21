# Pattern: Sliding Window — fixed size window + frequency array matching
# Trigger: "permutation/anagram exists in string" = fixed window = compare char frequencies

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1Count, s2Count = [0] * 26, [0] * 26

        # initialize frequency arrays for first window
        for i in range(len(s1)):
            s1Count[ord(s1[i]) - ord('a')] += 1
            s2Count[ord(s2[i]) - ord('a')] += 1

        # count how many characters already match between windows
        matches = 0
        for i in range(26):
            matches += (1 if s1Count[i] == s2Count[i] else 0)

        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26:    # all 26 chars match = permutation found
                return True

            # add new character from right
            index = ord(s2[r]) - ord('a')
            s2Count[index] += 1
            if s1Count[index] == s2Count[index]:
                matches += 1     # this char now matches
            elif s1Count[index] + 1 == s2Count[index]:
                matches -= 1     # this char just became mismatched

            # remove old character from left
            index = ord(s2[l]) - ord('a')
            s2Count[index] -= 1
            if s1Count[index] == s2Count[index]:
                matches += 1     # this char now matches again
            elif s1Count[index] - 1 == s2Count[index]:
                matches -= 1     # this char just became mismatched
            l += 1

        return matches == 26     # check last window