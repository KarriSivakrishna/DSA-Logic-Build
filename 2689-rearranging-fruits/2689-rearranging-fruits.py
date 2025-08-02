class Solution:
    def minCost(self, basket1: List[int], basket2: List[int]) -> int:
        count=Counter(basket1+basket2)
        for c in count:
            if count[c]%2:
                return -1

            count[c]>>=1

        basket11=list((Counter(basket1)-count).elements())
        basket21=list((Counter(basket2)-count).elements())
        cost=min(min(basket1),min(basket2))
        basket=sorted(basket11+basket21)

        return sum(min(cost+cost,basket[i]) for i in range(len(basket11)))