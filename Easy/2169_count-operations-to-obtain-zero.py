# Problem 2169: Count Operations to Obtain Zero
# Difficulty: Easy
class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        if not num1 or not num2:
            return 0
        count = 1
        while True:
            if num1 == num2:
                return count
            if num1 > num2:
                num1 = num1 - num2
            else:
                num2 = num2 - num1
            count += 1