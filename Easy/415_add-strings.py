# Problem 415: Add Strings
# Difficulty: Easy
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        ans = ""
        if len(num1) < len(num2):
            num_zeroes = len(num2) - len(num1)
            num1 = ('0' * num_zeroes) + num1

        elif len(num1) > len(num2):
            num_zeroes = len(num1) - len(num2)
            num2 = ('0' * num_zeroes) + num2

        over = False
        for i in range(len(num1) - 1, -1, -1):
            dig_one = (ord(num1[i]) - ord('0')) + (1 if over else 0)
            dig_two = (ord(num2[i]) - ord('0'))
            sum = dig_one + dig_two
            if sum >= 10:
                sum = sum % 10
                over = True
            else:
                over = False
            ans = str(sum) + ans
        if over:
            ans = '1' + ans
        return ans