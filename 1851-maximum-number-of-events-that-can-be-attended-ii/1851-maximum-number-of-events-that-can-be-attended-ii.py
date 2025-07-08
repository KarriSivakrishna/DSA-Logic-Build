class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:

        events.sort()

        @cache
        def dfs(ind, c):

            if c == 0:
                return 0

            if ind >= len(events):
                return 0

            ans = 0
            ans = max(ans, dfs(ind + 1, c))

            l = ind
            r = len(events) - 1

            while l <= r:
                
                mid = (l + r) // 2

                if events[mid][0] > events[ind][1]:
                    r = mid - 1
                else:
                    l = mid + 1

            ans = max(ans, events[ind][2] + dfs(l, c - 1 ))

            return ans
        
        return (dfs(0, k))
        