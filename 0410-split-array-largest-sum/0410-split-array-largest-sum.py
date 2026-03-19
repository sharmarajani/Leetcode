class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        low, high = max(nums) , sum(nums)
        def can_split(max_num):
            curr_sum = 0
            subarray =1
            for num in nums:
                if curr_sum + num > max_num:
                    subarray+=1
                    curr_sum = num
                else:
                    curr_sum+=num
            return subarray <=k

        while low <= high:
            mid = (low+high)//2
            if can_split(mid):
                ans = mid
                high= mid - 1
            else:
                low = mid +1
        return ans
        