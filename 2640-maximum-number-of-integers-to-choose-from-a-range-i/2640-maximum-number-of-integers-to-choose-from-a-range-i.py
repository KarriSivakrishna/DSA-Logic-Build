class Solution:
    def maxCount(self, banned: list[int], n: int, maxSum: int) -> int:
        banned_set = set(banned)
        sum_, count = 0, 0
        for i in range(1, n + 1):
            if i not in banned_set and sum_ + i <= maxSum:
                count += 1
                sum_ += i
        return count