class Solution:
    def isValid(self, word: str) -> bool:
        if len(word) < 3:
            return False
        if not word.isalnum():
            return False
        cntV, cntC = 0, 0
        for char in set(word):
            if char.isalpha():
                if char in "aeiouAEIOU":
                    cntV += 1
                else:
                    cntC += 1
        return cntV > 0 and cntC > 0