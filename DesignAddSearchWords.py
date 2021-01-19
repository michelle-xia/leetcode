class TrieNode:
    
    def __init__(self, val):
        self.children = dict()
        self.val = val
        self.end = False

class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = TrieNode(None)

    def addWord(self, word):
        node = self.head
        for c in word:        
            if not c in node.children:
                newNode = TrieNode(c)
                node.children[c] = newNode
            node = node.children[c]
        node.end = True

    def search(self, word):
        def dfs(word, node):
            for i, c in enumerate(word):
                if c == '.':
                    for ch in node.children:
                        if dfs(word[i+1:], node.children[ch]):
                            return True
                if not c in node.children:
                    return False
                node = node.children[c]
            return node.end
        node = self.head
        return dfs(word, node)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)