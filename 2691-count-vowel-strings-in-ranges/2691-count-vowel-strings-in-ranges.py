class Solution:
    def vowelStrings(self, a: List[str], q: List[List[int]]) -> List[int]:
        return (p:=[0,*accumulate({s[0],s[-1]}<{*'aeiou'} for s in a)]) and [p[r+1]-p[l] for l,r in q]