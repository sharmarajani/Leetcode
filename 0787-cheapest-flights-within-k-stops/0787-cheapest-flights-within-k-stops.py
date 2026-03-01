class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # Bellman Ford can deal with -ve weights and Djikstra's can't
        Prices = [float("inf")]  * n
        Prices[src] = 0

        for i in range(k+1):
            tmpPrice = Prices.copy()
            for s, d, p in flights: ## Src, dest, prices
                if Prices[s] == float("inf"):
                    continue
                if Prices[s] + p < tmpPrice[d]:
                    tmpPrice[d] = Prices[s] + p
            Prices = tmpPrice
        
        return -1 if Prices[dst] == float("inf") else Prices[dst]
                
            


