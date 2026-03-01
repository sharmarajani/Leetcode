class Solution:
    class TrieNode:
        def __init__(self):
            self.children = [None] * 26
            self.isEnd = False
    def __init__(self):
        self.root = self.TrieNode()

    def longestWord(self, words: List[str]) -> str:
        
        def insert( alpha):
            curr = self.root
            for i in alpha:
                index = ord(i) - ord('a')
                if curr.children[index] == None:
                    curr.children[index] = self.TrieNode()
                curr= curr.children[index]
            curr.isEnd = True

        def validWord( word):
            curr = self.root
            for char in word:
                index = ord(char) - ord('a')
                curr = curr.children[index]
                if curr.isEnd == False:
                    return False
            return True


        for alpha in words:
            insert( alpha)
        words.sort()
        longest = ""

        for word in words:
            if validWord(word):
                if len(word) > len(longest):
                    longest = word
        return longest
        