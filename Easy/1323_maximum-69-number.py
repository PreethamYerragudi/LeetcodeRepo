# Problem 1323: Maximum 69 Number
# Difficulty: Easy
class Solution:
    def maximum69Number (self, num: int) -> int:
        arr = list(str(num))
        try:
            arr[arr.index('6')] = '9'
        except:
            pass
        return int("".join(arr))
