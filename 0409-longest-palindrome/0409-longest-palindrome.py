class Solution:
    def longestPalindrome(self, s: str) -> int:
        hmap ={}
        res= 0
        odd_found = 0
        hmap = Counter(s)
        for i in hmap:
            if hmap[i] % 2 ==0:
                res+= hmap[i]
            else:
                res+=(hmap[i]-1)
                odd_found+=1
                
        if odd_found:
            res += 1
        return res
        