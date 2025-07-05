class Solution:
    def findLucky(self, arr: List[int]) -> int:
        c=Counter(arr)
        result=-1
        for i in arr:
            if i==c[i]:
                result=max(result,i)
        return result