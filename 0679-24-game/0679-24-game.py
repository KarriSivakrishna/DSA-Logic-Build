class Solution:
    def judgePoint24(self, cards):
        def compute(a, b, op):
            return a + b if op == 0 else a - b if op == 1 else a * b if op == 2 else a / b

        def solve(nums):
            nonlocal solCount
            if len(nums) == 1:
                if goal - e < nums[0] < goal + e: solCount += 1
                return
            if solCount > 0: return
            for i in range(len(nums)):
                for j in range(len(nums)):
                    if i == j: continue
                    for op in range(3 + (nums[j] != 0)):
                        if i > j and op % 2 == 0: continue
                        nums2 = [compute(nums[i], nums[j], op)] + [nums[k] for k in range(len(nums)) if k != i and k != j]
                        solve(nums2)

        e, goal, solCount = 10**-5, 24, 0
        solve(cards)
        return solCount > 0
 