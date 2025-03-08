class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        result=float("inf")
        for i in range(len(blocks)-k+1):
            window=blocks[i:i+k]
            D=window.count("W")
            result=min(D,result)
        return result
