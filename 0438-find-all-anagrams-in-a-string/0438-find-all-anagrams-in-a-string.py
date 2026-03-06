class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        hmapP = Counter(p)
        hmapS = Counter()
        res = []
        for i in range(len(s)):
            hmapS[s[i]]+=1
            if i >= len(p):
                if hmapS[s[i-len(p)]] == 1:
                    del hmapS[s[i-len(p)]]
                else:
                    hmapS[s[i-len(p)]]-=1
            
            if hmapP == hmapS:
                res.append(i-len(p) + 1)
        return res

        