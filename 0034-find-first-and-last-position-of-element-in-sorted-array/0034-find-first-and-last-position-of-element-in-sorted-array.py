lowerB = 0
class Solution:
    
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        lowerB = self.findLBound(nums, target, True)
        if lowerB == -1:
            return [-1, -1]
        upperB = self.findRBound(nums, target, False)
        return (lowerB, upperB)

    def findLBound(self, nums, target, isFirst):
        l, h = 0, len(nums)-1
        while l <= h:
            mid = (l+h)//2
            if nums[mid] == target:
                if mid==0 or nums[mid-1] != target:
                    return mid
                else:
                    h = mid -1
            elif nums[mid] > target :
                h = mid-1
            else:
                l = mid +1
        return -1
    
    def findRBound(self, nums, target, isFirst):
        l, h = lowerB , len(nums)
        while l <= h:
            mid = (l+h)//2
            if nums[mid] == target:
                if mid==len(nums)-1 or nums[mid+1] != target:
                    return mid
                else:
                    l = mid + 1
            elif nums[mid] > target :
                h = mid-1
            else:
                l = mid +1
        return -1

        