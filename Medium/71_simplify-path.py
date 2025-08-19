# Problem 71: Simplify Path
# Difficulty: Medium
class Solution:
    def simplifyPath(self, path: str) -> str:
        
        split_path = path.split("/")
        final_path = ["/"]
        print(split_path)
       
        for x in split_path:
            if x == '..':
                if len(final_path) <= 1:
                    continue
                else:
                    final_path.pop()
                    final_path.pop()
            elif x == '.' or x == '':
                continue
            else:
                final_path.append(x)
                final_path.append('/')
            
            
        if final_path[-1] == '/' and len(final_path) > 1:
            final_path.pop()
            
        return "".join(final_path)