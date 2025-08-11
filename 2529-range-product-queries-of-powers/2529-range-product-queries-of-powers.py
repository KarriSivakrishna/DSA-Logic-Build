from typing import List

class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        MOD = 10**9 + 7

        a = bin(n)[2:]
        result = []
        for i in range(len(a) - 1, -1, -1):
            if a[i] == '1':
                power = len(a) - 1 - i
                result.append(2 ** power % MOD)
        
        l = []
        for query in queries:
            a_idx, b_idx = query
            d = 1
            for c in range(a_idx, b_idx + 1):
                d = (d * result[c]) % MOD
            l.append(d)
        return l