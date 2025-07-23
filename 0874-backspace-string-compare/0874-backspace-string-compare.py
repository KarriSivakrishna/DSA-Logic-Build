class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def build(string):
            result = []
            for char in string:
                if char == '#':
                    if result:
                        result.pop()
                else:
                    result.append(char)
            return result
        
        return build(s) == build(t)