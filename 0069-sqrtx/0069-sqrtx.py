class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0 or x == 1:
            return x

        start, end = 1, x // 2
        ans = 0

        while start <= end:
            mid = start + (end - start) // 2
            sq = mid * mid

            if sq == x:
                return mid
            elif sq < x:
                ans = mid
                start = mid + 1
            else:
                end = mid - 1

        return ans