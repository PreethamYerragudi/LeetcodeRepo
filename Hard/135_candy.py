# Problem 135: Candy
# Difficulty: Hard
class Solution:
    def candy(self, ratings: List[int]) -> int:
        res = [0 for _ in range(len(ratings))]
        copy = sorted([(ratings[i], i) for i in range(len(ratings))], reverse=True)
        while copy:
            v, i = copy.pop()
            val = 0
            if i - 1 >= 0 and ratings[i-1] < ratings[i]:
                val = max(val, res[i - 1])
            if i + 1 < len(ratings) and ratings[i+1] < ratings[i]:
                val = max(val, res[i + 1])
            res[i] = val + 1
        print(res)
        return sum(res)