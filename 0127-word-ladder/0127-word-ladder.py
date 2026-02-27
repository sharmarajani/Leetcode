class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        adj_list = collections.defaultdict(list)
        wordList.append(beginWord)
        for word in wordList:
            for alphabet in range(len(word)):
                pattern = word[:alphabet] + "*" + word[alphabet+1:]
                adj_list[pattern].append(word)
            

        q = deque([beginWord])
        res=1
        visit=set([beginWord])
        while q:
            for i in range(len(q)):
                word= q.popleft()
                if word == endWord:
                    return res
                for j in range(len(word)):
                    pattern = word[:j] + "*" + word[j+1:]
                    for nei in adj_list[pattern]:
                        if nei not in visit:
                            visit.add(nei)
                            q.append(nei)
            res+=1
        return 0




        