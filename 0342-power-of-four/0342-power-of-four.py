class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n <= 0:
            return False
        for i in range(32):
            if 4**i <= n:
                if 4**i ==n:
                    return True
            else:
                return False
                