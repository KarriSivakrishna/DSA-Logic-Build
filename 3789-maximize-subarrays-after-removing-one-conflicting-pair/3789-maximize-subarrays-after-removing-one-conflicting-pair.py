class Solution:
    def maxSubarrays(self, n: int, conflictingPairs: list[list[int]]) -> int:
        validSubarrays = 0
        maxLeft = 0
        secondMaxLeft = 0
        gains = [0] * (n + 1)
        conflicts = [[] for _ in range(n + 1)]

        for a, b in conflictingPairs:
            l, r = min(a, b), max(a, b)
            conflicts[r].append(l)

        for r in range(1, n + 1):
            for l in conflicts[r]:
                if l > maxLeft:
                    secondMaxLeft = maxLeft
                    maxLeft = l
                elif l > secondMaxLeft:
                    secondMaxLeft = l

            validSubarrays += r - maxLeft
            gains[maxLeft] += maxLeft - secondMaxLeft

        return validSubarrays + max(gains)
