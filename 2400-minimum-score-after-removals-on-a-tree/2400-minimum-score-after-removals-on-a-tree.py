class Solution:
    def minimumScore(self, nums, edges):
        dict1 = defaultdict(list)

        for i,j in edges:
            dict1[i].append(j)
            dict1[j].append(i)

        @lru_cache(None)
        def dfs(root,parent):
            res = []
            val = nums[root]

            for neighbor in dict1[root]:
                if neighbor != parent:
                    cur = dfs(neighbor,root)
                    res.extend(cur)
                    val ^= cur[-1]

            res.append(val)

            return res

        min_val = float("inf")

        for x,y in edges:
            left_xors = dfs(x,y)
            right_xors = dfs(y,x)
            left_val = left_xors[-1]
            right_val = right_xors[-1]

            for l1 in left_xors[:-1]:
                l2 = left_val^l1
                min_val = min(min_val,max(l1,l2,right_val)-min(l1,l2,right_val))
                
            for r1 in right_xors[:-1]:
                r2 = right_val^r1
                min_val = min(min_val,max(r1,r2,left_val)-min(r1,r2,left_val))

        return min_val



        

        


