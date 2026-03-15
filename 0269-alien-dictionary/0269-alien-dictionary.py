class Solution:
    def alienOrder(self, words: List[str]) -> str:
        hmap =defaultdict(set)
        # for i in range(len(words)):
        #     if words[i] not in hmap:
        #         hmap[words[i]
        
        indegree = {ch:0 for word in words for ch in word}

        for i in range(len(words)-1):
            w1, w2 = words[i] , words[i+1]
            m,n = len(w1) , len(w2)
            min_len = min(m,n)
            if w1 > w2 and w1.startswith(w2):
                return ""
            for char in range(min_len):
                if w1[char] != w2[char]:
                    if w2[char] not in hmap[w1[char]]:
                        hmap[w1[char]].add(w2[char])
                        indegree[w2[char]]+=1
                    break
        print(hmap, indegree)
        q =deque([i for i in indegree if indegree[i] == 0])
        result = []
        
        while q:
            ch = q.popleft()
            result.append(ch)
            for i in hmap[ch]:
                indegree[i]-=1
                if indegree[i]==0:
                    q.append(i)
        
        return "".join(result) if len(result) == len(indegree) else  ""

        