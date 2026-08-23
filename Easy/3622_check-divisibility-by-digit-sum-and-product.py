# Problem 3622: Check Divisibility by Digit Sum and Product
# Difficulty: Easy
class Solution:
    def checkDivisibility(self, n: int) -> bool:
        digit_sum = 0
        digit_prod = 1
        temp = n
        while temp:
            d = temp % 10
            digit_sum += d
            digit_prod *= d
            temp //= 10
        return not (n % (digit_sum + digit_prod))