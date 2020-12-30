class Solution:
    def findLadders(self, beginWord, endWord, wordList):
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
                for letter in range('a', 'z'):
                    tmp[i] = letter

                    if tmp in wordList:

                        # only add if not same level or above
                        if tmp not in visited or visited[tmp] > visited[word]:

                            if word not in adjacency_map:
                                adjacency_map[word] = [tmp]

                            else:
                                adjacency_map[word].append(tmp)
                            visited[tmp] = visited[word] + 1
                            q.append(tmp)
                        
        # depth first search for all paths to the final word
        