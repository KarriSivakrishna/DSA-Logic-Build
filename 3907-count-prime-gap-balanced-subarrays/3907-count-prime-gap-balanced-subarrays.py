from sortedcontainers import SortedList

class Solution:
    def primeSubarray(self, nums: List[int], k: int) -> int:
        def get_primes(n):
            if n == 1:
                return []
            sieve = [True] * (n + 1)
            sieve[0] = sieve[1] = False
            for i in range(4, n + 1, 2):
                sieve[i] = False
            for p in range(3, round((n + 1) ** 0.5) + 1, 2):
                if sieve[p]:
                    for elem in range(p ** 2, n + 1, 2 * p):
                        sieve[elem] = False
            return [
                i
                for i, is_prime in enumerate(sieve)
                if is_prime
            ]

        unique_primes = set(get_primes(max(nums)))
        indexes = [
            (i, elem)
            for i, elem in enumerate(nums)
            if elem in unique_primes
        ]

        l = 0
        state = SortedList()
        result = 0

        for r, (j, b) in enumerate(indexes):
            # update state
            state.add(b)
            while len(state) > 1 and state[-1] - state[0] > k:
                state.remove(indexes[l][1])
                l += 1

            # calculate size of borders of current (correct) window
            if l != r:
                # first prime element in window (inclusive)
                # + non-prime elements left over from them
                # (to next prime element)
                if l == 0:
                    left = indexes[l][0] + 1
                else:
                    left = indexes[l][0] - indexes[l - 1][0]
                    
                # elements
                # from first prime element in window (not inclusive)
                # to penultimate prime number (inclusive)
                inner = indexes[r - 1][0] - indexes[l][0]

                # last prime element in window (inclusive)
                # + non-prime elements right over from them
                # (to next prime element)
                if r == len(indexes) - 1:
                    right = len(nums) - j
                else:
                    right = indexes[r + 1][0] - j

                result += (left + inner) * right
        
        return result