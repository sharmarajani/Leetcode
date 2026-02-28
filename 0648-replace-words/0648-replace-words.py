class Solution:
    class TrieNode:
        def __init__(self):
            self.children=[None] * 26
            self.isEnd= False
    def __init__(self):
        self.root = self.TrieNode() 
    

    def insert(self, word):
        curr = self.root
        for char in word:
            index = ord(char) - ord('a')
            if curr.children[index] is None:
                curr.children[index] = self.TrieNode()
            curr = curr.children[index]
        curr.isEnd = True
            
    def searchRoot(self, word):
        curr = self.root
        prefix = ""
        for char in word:
            index = ord(char) - ord('a')
            if curr.children[index] is None:
                return word
            prefix += char
            curr = curr.children[index]
            if curr.isEnd:
                return prefix
        return word

    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        for word in dictionary:
            self.insert(word)

        # Step 2: Process sentence
        words = sentence.split()
        result = []

        for word in words:
            result.append(self.searchRoot(word))

        return " ".join(result)
        result = []
        