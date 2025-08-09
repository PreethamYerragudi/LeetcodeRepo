# Problem 3042: Count Prefix and Suffix Pairs I
# Difficulty: Easy
class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        def isPrefixAndSuffix(str1, str2):
            if str2[0:len(str1)] != str1:
                return False
            return (str2[len(str2) - len(str1):len(str2)] == str1)
        num = 0
        for j in range(len(words)):
            for i in range(j):
                if isPrefixAndSuffix(words[i], words[j]):
                    num += 1
        return num
                