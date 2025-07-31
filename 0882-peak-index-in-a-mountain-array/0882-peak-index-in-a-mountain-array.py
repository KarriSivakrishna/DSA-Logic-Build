class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        left = 0
        right = len(arr)-1
        while left < right:
            m = (left+right)//2

            if arr[m-1] > arr[m]:
                right = m
            elif arr[m] < arr[m+1]:
                left = m
            else:
                return m