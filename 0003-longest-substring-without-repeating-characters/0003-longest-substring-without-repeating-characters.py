class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        slow, fast = 0 , 0
        res, set1 = 0, set()
        while fast< len(s):
            while s[fast] in set1:
                set1.remove(s[slow])
                slow+=1
            set1.add(s[fast])
            res= max(res, fast-slow+1)
            fast+=1
        return res
