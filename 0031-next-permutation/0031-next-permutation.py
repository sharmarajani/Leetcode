class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if n<1:
            return 
        temp = -1
        for i in range(len(nums)-2, -1 , -1):
            if nums[i] < nums[i+1]:
                temp = i
                break
                # nums[i], nums[i-1] = nums[i-1], nums[i]
                
        if temp!=-1:
            for i in range(len(nums)-1, temp , -1 ):
                if nums[i] > nums[temp]:
                    nums[i], nums[temp] = nums[temp], nums[i]
                    break
        def reverse(nums, l, h):
            while l < h:
                nums[l], nums[h] = nums[h], nums[l]
                l+=1
                h-=1
            

        reverse(nums, temp+1, n-1)

        

        
        

