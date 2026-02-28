class Trie:
    
    class TrieNode:
        def __init__(self):
            self.children = [None] * 26
            self.isEnd = False

    def __init__(self):
        self.root = self.TrieNode()        

    def insert(self, word: str) -> None:
        curr = self.root
        for alpha in word:
            index = ord(alpha)- ord('a')
            if curr.children[index] is None:
                curr.children[index] = self.TrieNode()
            curr = curr.children[index]
        curr.isEnd = True
    def search(self, word: str) -> bool:
        curr = self.root
        for alpha in word:
            index = ord(alpha) - ord('a')
            if curr.children[index] is None:
                return False
            curr = curr.children[index]
        return curr.isEnd
        

    def startsWith(self, prefix: str) -> bool:
        curr= self.root
        for alpha in prefix:
            index = ord(alpha) - ord('a')
            if curr.children[index] is None:
                return False
            curr= curr.children[index]
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)