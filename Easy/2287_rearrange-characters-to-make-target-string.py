# Problem 2287: Rearrange Characters to Make Target String
# Difficulty: Easy
class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        count = Counter(s)
        ans = 0
        while True:
            for char in target:
                if count[char] <= 0:
                    return ans
                count[char] -= 1
            ans += 1