# Problem 3: Longest Substring Without Repeating Characters
# Difficulty: Medium
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        #hashmap in this case is a dictionary; so just think dictionary and what its purposes are 
        
        string_dict = defaultdict(int)
        left = 0
        ans = 0
        
        for i in range(len(s)): #will iterate through string, i is index 
            if s[i] in string_dict: #if char already existed 
                    target_index = string_dict[s[i]]   #get location of repeat
                    left_copy = left
                    left = string_dict[s[i]] + 1  #update left to index of repeat + 1 
                    

                    while target_index >= left_copy: #now delete everything from repeat to the old left
                        del string_dict[s[target_index]]
                        target_index -= 1 

                     
            ans = max(ans, i - left + 1) #update greatest length, accounting for new left as well 
            string_dict[s[i]] = i #atp, there are no repeats, so can just add char
        
        return ans 
                
        
                
                
                