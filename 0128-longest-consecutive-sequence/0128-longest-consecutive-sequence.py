class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        long_streak = 0
        for i  in num_set:
            if i -1 not in num_set :
                curr_num = i
                curr_streak = 1
                while curr_num + 1 in num_set:
                    curr_streak +=1
                    curr_num +=1
                long_streak = max(long_streak, curr_streak)
        return  long_streak    