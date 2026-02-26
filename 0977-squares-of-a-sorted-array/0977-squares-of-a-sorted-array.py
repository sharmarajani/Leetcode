class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result =[0] * len(nums)
        left = 0
        right = len(nums)-1
        for i in range(n-1, -1 , -1):
            if abs(nums[left]) < abs(nums[right]):
                sq = nums[right]
                right-=1
            else:
                sq= nums[left]
                left+=1
            result[i] = sq * sq
        return result
        