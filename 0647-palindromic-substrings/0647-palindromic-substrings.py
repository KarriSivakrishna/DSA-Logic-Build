class Solution:
    def countSubstrings(self, s: str) -> int:
        n=len(s)
        count = 0
        for i in range(n):
            local_count_odd=0
            for j in range(n):
                if i-j<0 or i+j>=n or s[i-j]!=s[i+j]:
                    break
                local_count_odd+=1

            local_count_even=0
            for j in range(n):
                if i-j<0 or i+j+1>=n or s[i-j]!=s[i+j+1]:
                    break
                local_count_even+=1

                        
            count+=(local_count_odd+local_count_even)
        return count

        