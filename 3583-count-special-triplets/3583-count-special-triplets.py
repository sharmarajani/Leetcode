class Solution:
    def specialTriplets(self, nums: List[int]) -> int:
        right_map = collections.Counter(nums)
        left_map = collections.Counter()
        n = len(nums)
        Mod = 10**9 +7
        total_trip = 0
        count = 0
        for i in range(n):
            curr_val = nums[i]
            right_map[curr_val] -=1
            target = curr_val *2
            if target in left_map and target in right_map:
                count = (left_map[target] * right_map[target]) % Mod
                total_trip = (total_trip + count) % Mod
            left_map[curr_val]+=1
        
        return total_trip
        