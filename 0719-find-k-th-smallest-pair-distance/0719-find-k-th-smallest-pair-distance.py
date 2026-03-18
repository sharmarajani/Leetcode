class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        n =len(nums)
        nums.sort()
        low, hi = 0, nums[-1] - nums[0]
        def check_pairs_within(mid):
            count, l = 0,0
            for r in range(n):
                while nums[r] -nums[l] > mid:
                    l+=1
                count+= (r-l)
            return count
        while low < hi:
            mid = (low+hi)//2
            if check_pairs_within(mid)>=k:
                hi = mid
            else:
                low = mid+1
        return low        