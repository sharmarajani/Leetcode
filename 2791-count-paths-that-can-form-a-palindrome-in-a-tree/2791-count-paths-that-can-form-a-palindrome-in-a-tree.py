class Solution:
    def countPalindromePaths(self, parent: List[int], s: str) -> int:
        adj = defaultdict(list)
        for i in range(1,len(parent)):
            adj[parent[i]].append(( i, s[i] ))
        masks={0:1}
        self.ans= 0
        def dfs(u, curr_mask):
            for v, char in adj[u]:
               new_mask = curr_mask ^( 1 <<(ord(char) - ord('a')))
               self.ans += masks.get(new_mask, 0)
               for i in range(26):
                    self.ans += masks.get(new_mask ^ (1 <<i), 0)
               masks[new_mask] = masks.get(new_mask,0) + 1
               dfs(v, new_mask)
        dfs(0,0)
        return self.ans
        