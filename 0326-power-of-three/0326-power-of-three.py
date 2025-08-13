class Solution(object):
    def isPowerOfThree(self, n):
        return n>0 and (3**19)%n==0
        """
        :type n: int
        :rtype: bool
        """
        