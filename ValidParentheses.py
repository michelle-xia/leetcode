class Solution:
    def isValid(self, s):
        if s is None:
            return
        
        d = {'(': ')', '{': '}', '[': ']'}
        stack = []      
        for c in s:
            if stack and stack[-1] in d and d[stack[-1]] == c:
                del stack[-1]
            else:
                stack.append(c)
        return not stack