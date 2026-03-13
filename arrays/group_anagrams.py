# Pattern: HashMap + Sorting — group words by their sorted signature as key
# Trigger: "group anagrams" = categorize words = find common identity = sorted chars as key

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for word in strs:
            key = "".join(sorted(word))  # anagrams share the same sorted key
            groups[key].append(word)
        return list(groups.values())
    