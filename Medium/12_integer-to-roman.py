# Problem 12: Integer to Roman
# Difficulty: Medium
class Solution:
    def intToRoman(self, num: int) -> str:
        ans = ""
        dic = {
            1000 : 'M',
            500 : 'D',
            100 : 'C',
            50 : 'L',
            10 : 'X',
            5 : 'V',
            1 : 'I'
            }
        
        digit = 10 ** (len(str(num)) - 1)
        while digit >= 1:
            val = int(num / digit)
            if digit == 1000:
                ans += dic[digit] * val
            else:
                if val == 9:
                    ans +=  dic[digit] + dic[10 * digit]
                elif val == 4:
                    ans +=  dic[digit] + dic[5 * digit]
                else:
                    if val >= 5:
                        ans += dic[digit * 5] + dic[digit] * (val - 5)
                    else:
                        ans += dic[digit] * val
            num = num % digit
            digit = int(digit / 10)
        return ans
