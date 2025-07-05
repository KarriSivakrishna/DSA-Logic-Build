class Solution:
    def findLucky(self, arr: List[int]) -> int:
        c=Counter(arr)
        maxi=-1
        for i in arr:
            if i==c[i]:
                maxi=max(maxi,i)
        return maxi