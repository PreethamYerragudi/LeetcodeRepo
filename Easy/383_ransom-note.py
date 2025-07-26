# Problem 383: Ransom Note
# Difficulty: Easy
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        counts_ransom_note = Counter(ransomNote)
        counts_magazine = Counter(magazine)
        
        for x in ransomNote: #iterate through the string and account for each character from the 
            counts_magazine[x] -= 1
        
        for value in counts_magazine.values():
            if value < 0: 
                return False
             
        #if code survived until here means availability is there
        return True