class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        
        output = []
        for query in queries:
            q_idx = 0
            p_idx = 0
            while q_idx < len(query):
                if p_idx < len(pattern) and query[q_idx] == pattern[p_idx]:
                    q_idx += 1
                    p_idx += 1
                else:
                    if query[q_idx].isupper():                        
                        break
                    q_idx += 1
            if q_idx >= len(query) and p_idx >= len(pattern):
                output.append(True)
            else:
                output.append(False)

        
        return output