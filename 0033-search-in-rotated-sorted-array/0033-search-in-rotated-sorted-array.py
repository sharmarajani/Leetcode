class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, hi = 0, len(nums)-1
        while l <= hi:
            mid = (l+hi) //2
            if nums[mid]==target:
                return mid

            elif nums[mid] >= nums[l]:
                if target >= nums[l] and target < nums[mid]:
                    hi = mid-1
                else:
                    l = mid +1
            
            else:
                if target >nums[mid] and target <= nums[hi]:
                    l = mid + 1
                else:
                    hi = mid-1
        return -1


     