from collections import defaultdict

class Solution:
    def makeFancyString(self, s: str) -> str:
        if len(s) < 3:
            return s
        
        result = []
        prev_char = s[0]
        count = 1
        result.append(prev_char)
        
        for char in s[1:]:
            if char == prev_char:
                count += 1
                if count < 3:
                    result.append(char)
            else:
                prev_char = char
                count = 1
                result.append(char)
        
        return ''.join(result)