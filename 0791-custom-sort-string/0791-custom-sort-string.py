class Solution:
    def customSortString(self, order: str, s: str) -> str:
        hmap_s = Counter(s)
        res = []

        for char in order:
            res.append(char * hmap_s[char])
            hmap_s[char] = 0

        for char in hmap_s:
            res.append(char * hmap_s[char]) 
        
        return "".join(res)

        