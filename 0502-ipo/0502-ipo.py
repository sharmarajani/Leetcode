class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        projects = sorted(zip(capital, profits))
        max_heap = []
        i = 0

        for _ in range(k):
            while i<len(projects) and projects[i][0] <= w:
                heapq.heappush(max_heap , -projects[i][1])
                i+=1
            if max_heap:
                w+= -heapq.heappop(max_heap)
            else:
                break
        return w