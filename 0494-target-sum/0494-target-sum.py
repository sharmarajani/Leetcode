class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp ={}
        def backtrack(idx, rsum): 
            if idx == len(nums):
                return 1 if rsum == target else 0  
            if (idx, rsum) in dp:
                return dp[(idx,rsum)]
            dp[(idx,rsum)] = (backtrack(idx+1,rsum+ nums[idx]) + backtrack(idx+1 , rsum - nums[idx])) 
            return dp[(idx, rsum)]
        return backtrack(0,0)
        