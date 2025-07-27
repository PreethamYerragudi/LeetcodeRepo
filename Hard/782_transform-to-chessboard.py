# Problem 782: Transform to Chessboard
# Difficulty: Hard
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        
        #first initialize a dict 
        counts = defaultdict(int)
        
        #iterate through the stones 
        for stone in stones: 
            if stone in jewels: 
                counts[stone] += 1 #may be duplicate stones so need frequencies tracked 
                       
                       
        ans = sum(counts.values()) #get sum of every time there's a stone also in jewels 
        
        return ans 