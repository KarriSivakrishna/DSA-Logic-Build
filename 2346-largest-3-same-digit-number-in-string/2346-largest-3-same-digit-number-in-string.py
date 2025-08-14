class Solution:
    def largestGoodInteger(self, num: str) -> str:
        good_integers = []
        for i in range(len(num)-2):
            if num[i]==num[i+1]==num[i+2]:
                good_integers.append(num[i:i+3])
        return max(good_integers) if good_integers else ""


        