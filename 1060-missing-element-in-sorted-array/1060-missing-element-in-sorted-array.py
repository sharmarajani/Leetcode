class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        n = len(nums)
        l, r = 0, n-1
        while l <= r:
            mid= (l+r)//2
            missing = (nums[mid] - nums[0]) - mid
            if missing < k:
                l = mid + 1
            else:
                r = mid - 1
        return nums[0] + k + r

        
