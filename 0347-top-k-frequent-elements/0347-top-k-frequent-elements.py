class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hmap = Counter(nums)
        result =[]
        ans=[]
        for key, values in hmap.items():
            heapq.heappush(result , (values, key, ))
            if len(result) > k:
                heapq.heappop(result)
        for i in result:
            ans.append(i[1])
        return ans
        

        