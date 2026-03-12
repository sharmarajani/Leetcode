class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        # l, h = 0,1
        # if len(nums)<2:
        #     return(max(nums[0]), nums[1])
        # while 

        for i in range(len(nums) - 1):
            if  nums[i] > nums[i+1] : 
                return i
        return len(nums) -1 
