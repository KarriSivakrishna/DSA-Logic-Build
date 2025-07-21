class Solution:
    def customSortString(self, order: str, s: str) -> str:
        dict = Counter(s)
        res = []
        for o in order:
            if o in dict and dict[o] > 0:
                res.append(o*dict[o])
                dict[o] = 0

        for i,v in enumerate(dict):
            if dict[v] > 0:
                res.append(v*dict[v])
                dict[v] = 0

        return "".join(res)
