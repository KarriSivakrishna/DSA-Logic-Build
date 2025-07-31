class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i =j = 0
        x = ""
        while j<len(t) and i<len(s):
            if s[i] == t[j]:
                x += s[i]
                i+=1
                j+=1
            else:
                j+=1
        if x==s:
            return True
        return False