# Problem 49: Group Anagrams
# Difficulty: Medium
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groupings = {}
        ans = []
        for str in strs:
            key = "".join(sorted(str))
            if key not in groupings.keys():
                groupings[key] = []
            groupings[key].append(str)
        for value in groupings.values():
            ans.append(value)
        return ans