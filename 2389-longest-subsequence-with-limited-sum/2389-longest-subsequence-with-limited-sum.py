class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        ans= [] 
        nums.sort()
        for val in queries:
            count = 0
            for num in nums:
                if val >= num:
                    val-=num
                    count+=1
                else:
                    break
            ans.append(count)
        return ans
            

        