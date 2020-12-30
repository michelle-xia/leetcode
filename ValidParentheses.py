class Solution:
    def isValid(self, s):
        if s is None:
            return
        o = ['(', '{', '[']
        close = [')', '}', ']']
        stack = []

        for c in s:
            if c in o:
                stack.append(c)
            if c in close:
                if len(stack) == 0:
                    return False
                match = stack.pop()
                ind = o.index(match)
                if c != close[ind]:
                    return False
        if len(stack) > 0:
            return False
        return True