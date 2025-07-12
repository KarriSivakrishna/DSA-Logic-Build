class Solution:
    def intToRoman(self, num: int) -> str:
        val = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        roman = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']

        res = ''
        while num > 0:
            tnum = -1
            for i in range(len(val)):
                if val[i] <= num:
                    tnum = i
                    break
            if tnum != -1:
                res += roman[i] * (num // val[i])
                num %= val[i]

        return res