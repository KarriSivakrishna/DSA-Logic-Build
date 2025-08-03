class Solution:
    def maxTotalFruits(self, fruits: List[List[int]], startPos: int, k: int) -> int:
        res = l = curr = 0

        for r in range(len(fruits)):
            curr += fruits[r][1]
            while l <= r:
                lpos = fruits[l][0]
                rpos = fruits[r][0]
                if min(abs(lpos - startPos), abs(rpos - startPos)) + (rpos - lpos) <= k:
                    break
                curr -= fruits[l][1]
                l += 1

            res = max(res, curr)

        return res
        