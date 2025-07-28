class Solution:
    def partitionString(self, s: str) -> list[str]:
        seen = set()
        segments = []
        idx = 0
        n = len(s)
        while idx < n:
            seg = ''
            for j in range(idx, n):
                seg += s[j]
                if seg not in seen:
                    segments.append(seg)
                    seen.add(seg)
                    idx = j + 1
                    break
            else:
                break
        return segments