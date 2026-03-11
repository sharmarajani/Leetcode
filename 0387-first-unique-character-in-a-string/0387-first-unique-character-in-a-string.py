class Solution:
    def firstUniqChar(self, s: str) -> int:
        hmap = Counter(s)
        for i in range(len(s)):
            if hmap[s[i]]==1:
                return i
        return -1 
        