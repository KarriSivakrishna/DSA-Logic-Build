class Solution:

    def __init__(self, nums: List[int]):
        self.indexes = dict()
        for idx, num in enumerate(nums):
            if num not in self.indexes:
                self.indexes[num] = []
            self.indexes[num].append(idx)

    def pick(self, target: int) -> int:
        idx = random.randint(0, len(self.indexes[target]) - 1)
        return self.indexes[target][idx]


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)