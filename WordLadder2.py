from collections import defaultdict

class Solution:
    def findLadders(self, beginWord, endWord, wordList):
        # faster lookup time
        wordList = set(wordList)
        
        # initialize adjacency list with parent:child layers
        adjacency_map = defaultdict(set)
        
        # flag for when endWord is found
        stop = False
        
        # all letters in the alphabet
        alpha = 'qwertyuiopasdfghjklzxcvbnm'
        
        # first layer
        layer = set([beginWord])
        
        # remove beginWord from wordList
        wordList.discard(beginWord)
        
        # breadth first search to populate adjacency list with parent:child
        while layer and not stop:
            next_layer = set()
            
            for word in layer:
                for i in range(len(word)):
                    for letter in alpha:
                        nw = word[:i] + letter + word[i + 1:]
                        if nw in wordList:
                            next_layer.add(nw)
                            adjacency_map[word].add(nw)
                        if nw == endWord:
                            stop = True
            wordList -= next_layer
            layer = next_layer
        
        ans = []
        path = [beginWord]
        
		# find the paths with dfs
        def dfs(w):
            if w == endWord:
                ans.append(path[:])
            else:
                for nw in adjacency_map[w]:
                    path.append(nw)
                    dfs(nw)
                    path.pop()
                
        dfs(beginWord)
        
        return ans