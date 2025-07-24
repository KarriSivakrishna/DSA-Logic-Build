class Solution:
    def myAtoi(self, s: str) -> int:
        # Remove leading whitespace
        s = s.lstrip()
        if not s:
            return 0

        sign = 1
        i = 0
        # Check for sign
        if s[0] == '-':
            sign = -1
            i += 1
        elif s[0] == '+':
            i += 1

        num = 0
        # Convert digits
        while i < len(s) and s[i].isdigit():
            num = num * 10 + int(s[i])
            i += 1

        num *= sign
        # 32-bit integer bounds
        INT_MIN, INT_MAX = -2**31, 2**31 - 1
        if num < INT_MIN:
            return INT_MIN
        if num > INT_MAX:
            return INT_MAX
        return num
