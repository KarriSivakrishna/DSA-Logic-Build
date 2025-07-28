class Solution:
    def getEncryptedString(self, s: str, k: int) -> str:
        n = len(s)
        t = list(s)
        for i in range(n):
            # Update t[i] to be the character from s that is k positions ahead
            # Use (i + k) % n to wrap around the end of the string
            t[i] = s[(i + k) % n]
        return ''.join(t)