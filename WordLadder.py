class Solution:
    def ladderLength(self, beginWord, endWord, wordList):
        # faster lookup time
        wordList = set(wordList)
        
        # initialize adjacency list with parent:child
        adjacency_map = {} 
        
        # create list to track visited
        visited = {beginWord: 0}
        
        q = [beginWord]
        
        # breadth first search to populate adjacency list with parent:child
        while len(q) > 0:
            word = q.pop(0)         
            for i in range(len(word)):
                tmp = word
                for x in range(ord('a'), ord('z') + 1):
                    letter = chr(x)
                    tmp = list(tmp)
                    tmp[i] = letter
                    tmp = ''.join(tmp)

                    if tmp in wordList:

                        # only add if not same level or above
                        if tmp not in visited or visited[tmp] > visited[word]:

                            if word not in adjacency_map:
                                adjacency_map[word] = [tmp]

                            else:
                                adjacency_map[word].append(tmp)
                            visited[tmp] = visited[word] + 1
                            q.append(tmp)
                    tmp = word
        if endWord not in visited:
            return 0
        
        return visited[endWord] + 1