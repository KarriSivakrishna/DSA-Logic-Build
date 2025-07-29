class Solution:
    def smallestTrimmedNumbers(self, nums: List[str], queries: List[List[int]]) -> List[int]:
        i = 0
        res = []
        while i<len(queries):
            k = queries[i][0]
            trim = queries[i][1]
            copy = nums.copy()
            for idx, num in enumerate(nums):
                copy[idx] = int(num[-trim:])
            cpy = sorted([(num, i) for i, num in enumerate(copy)])

            res.append(cpy[k-1][1])
            i+=1
        return res