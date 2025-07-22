class Solution:
    def countPrimes(self, n: int) -> int:
        if n<=1:
            return 0
        primes = [True]*n
        primes[0]=primes[1]=False
        for i in range(2,int(n**0.5)+1):
            if primes[i] == True:
                for j in range(i*i,n,i):
                    primes[j]=False
        return primes.count(True)