class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hmap = {0:1}
        rsum = 0
        cnt=0
        for i in range(len(nums)):
            rsum+=nums[i]
            if rsum - k  in hmap:
                cnt += hmap[rsum-k]
            hmap[rsum] = hmap.get(rsum, 0) + 1
        return cnt



        