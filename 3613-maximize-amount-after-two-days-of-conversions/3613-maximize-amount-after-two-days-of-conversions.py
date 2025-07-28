class Solution:
    def maxAmount(self, initialCurrency: str, pairs1: List[List[str]], rates1: List[float], pairs2: List[List[str]], rates2: List[float]) -> float:

        # day1: val for different currency from EU
        # day2: val for different currenty from EU (reverse)

        from collections import defaultdict
        def buildGraph(pairs, rates):
            graph = defaultdict(list)
            for i in range(len(pairs)):
                u, v = pairs[i]
                graph[u].append((v, rates[i]))
                graph[v].append((u, 1/rates[i]))
            return graph

        graph1 = buildGraph(pairs1, rates1)
        graph2 = buildGraph(pairs2, rates2)

        def dfs(currency, graph, exchange):
            rate = exchange[currency]
            for neigh, rate2 in graph[currency]:
                if neigh not in exchange:
                    exchange[neigh] = rate * rate2
                    dfs(neigh, graph, exchange)

        exchange1 = {initialCurrency: 1}
        exchange2 = {initialCurrency: 1}

        dfs(initialCurrency, graph1, exchange1)
        dfs(initialCurrency, graph2, exchange2)

        res = 1
        for i in exchange1:
            if i in exchange2:
                res = max(res, exchange1[i] / exchange2[i])

        return res