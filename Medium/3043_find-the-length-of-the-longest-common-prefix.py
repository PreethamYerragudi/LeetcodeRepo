# Problem 3043: Find the Length of the Longest Common Prefix
# Difficulty: Medium
class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        prefixes = set()
        for num in arr1:
            new_num = num
            while new_num >= 1:
                prefixes.add(new_num)
                new_num = int(new_num / 10)
        print(prefixes)

        prefixes_two = set()
        for num in arr2:
            new_num = num
            while new_num >= 1:
                prefixes_two.add(new_num)
                new_num = int(new_num / 10)
        prefixes_two = sorted(prefixes_two, reverse = True, key=lambda a: len(str(a)))
        for num in prefixes_two:
            if num in prefixes:
                return len(str(num))
        return 0
