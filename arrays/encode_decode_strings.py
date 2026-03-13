# Pattern: Custom Encoding — encode length + delimiter before each word to avoid separator conflicts
# Trigger: "encode decode" = need separator that can't appear in words = encode the length instead

class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            # length of word + "#" + word itself
            # e.g. ["hello", "world"] → "5#hello5#world"
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        res, i = [], 0
        while i < len(s):
            j = i
            # find the "#" — everything before it is the length
            while s[j] != "#":
                j += 1
            # extract exact number of chars after "#" using length
            # safe even if word contains "#" — we use length not search
            length = int(s[i:j])
            res.append(s[j + 1: j + 1 + length])
            # move pointer to next encoded word
            i = j + 1 + length
        return res