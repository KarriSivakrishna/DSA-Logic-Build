class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        a=s+s
        if s in a[1:-1]:
            return True
        return False