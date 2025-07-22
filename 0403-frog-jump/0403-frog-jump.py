class Solution:
    def canCross(self, stones: List[int]) -> bool:
        n = stones[-1]
        hm = {}
        for i in range(len(stones)):
            hm[stones[i]] = i
        dp = {}
        def helper(i,k):
            if i not in hm:
                return False
            if i==n:
                return True
            if (i,k) in dp:
                return dp[(i,k)]
            for j in [k-1,k,k+1]:
                if i+j>i and helper(i+j,j):
                    dp[(i,k)] = True
                    return True
            dp[(i,k)] = False
            return False
        if stones[1]==1:
            return helper(1,1)
        else:
            return False