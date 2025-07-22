import bisect
class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        s = []
        mapp = {}
        for i in range(len(intervals)):
            s.append(intervals[i][0])
            mapp[intervals[i][0]] = i

        s.sort()

        res = []
        for i , j in intervals:
            idx = bisect.bisect_left(s, j)
            if idx == len(s):
                res.append(-1)
            else:
                res.append(mapp[s[idx]])
        
        return res

        