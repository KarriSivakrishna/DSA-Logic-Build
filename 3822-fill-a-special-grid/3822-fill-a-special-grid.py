class Solution:
    def specialGrid(self, n: int) -> List[List[int]]:
        if n == 0: return [[0]]

        def assign(nums):
            if len(nums) == 1:
                return [[nums[0]]]
            else:
                L = len(nums)
                first = L//4
                second = (L//4) * 2
                third = (L//4) * 3
                tr = assign(nums[:first])
                br = assign(nums[first:second])
                bl = assign(nums[second:third])
                tl = assign(nums[third:L])

                m = len(tr)
                top = []
                button = []
                for i in range(m):
                    top.append(tl[i] + tr[i])
                    button.append(bl[i] + br[i])
                return top + button

        return assign(list(range((2**(2*n)))))
