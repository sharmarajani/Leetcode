class Solution:
    def longestAwesome(self, s: str) -> int:
        curr_mask = 0
        hmap = {0:-1}
        max_len = 0
        for i in range(len(s)):
            digit = int(s[i])
            curr_mask ^= (1<< digit)
            if curr_mask   in hmap:
                max_len = max(max_len , i-hmap[curr_mask])
            else:
                hmap[curr_mask] = i
            
            for d in range(10):
                check_mask = curr_mask ^(1 << d)
                if check_mask in hmap:
                    max_len = max(max_len , i-hmap[check_mask])
            
        return max_len

        