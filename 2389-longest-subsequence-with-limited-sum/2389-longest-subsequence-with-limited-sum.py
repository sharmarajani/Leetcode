class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        ans= [] 
        nums.sort()
        for i in range(1, len(nums)):
            nums[i]= nums[i-1] + nums[i]
        for i in range(len(queries)):
            index = bisect.bisect_right(nums , queries[i])
            ans.append(index)
        return ans
            

        