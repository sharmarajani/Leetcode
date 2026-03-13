class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        hmap = {}
        for i in range(len(order)):
            hmap[order[i]] = i+1
        def isValid(first , second):
            for i in range(min(len(first), len(second))):
                if first[i] != second[i]:
                    return hmap[first[i]]  > hmap[second[i]]
            return len(first) > len(second)
        for i in range(len(words) - 1):
            if isValid(words[i] , words[i+1]):
                return False
        return True
        