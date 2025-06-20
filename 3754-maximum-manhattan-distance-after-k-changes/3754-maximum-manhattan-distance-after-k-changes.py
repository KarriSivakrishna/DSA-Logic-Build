class Solution:
    def maxDistance(self, s: str, k: int) -> int:
        # a, b are main direction else direction enemy
        def solve(a, b, s, k):
            dist = 0
            mx = 0

            for ch in s:
                if ch == a or ch == b:
                    dist += 1
                else:
                    if k > 0:
                        k -= 1
                        dist += 1
                    else:
                        mx = max(mx, dist)
                        dist -= 1

            mx = max(mx, dist)
            return mx

        if k == len(s):
            return k

        # good direction
        nw = solve('N', 'W', s, k)
        ne = solve('N', 'E', s, k)
        sw = solve('S', 'W', s, k)
        se = solve('S', 'E', s, k)

        return max(nw, ne, sw, se)