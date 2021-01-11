from collections import Counter
class Solution:
    def reorganizeString(self, S):
        if S is None or len(S) == 0:
            return ""
             
        counter = Counter(S)
        
        if max(counter.values()) > (len(S) + 1) // 2:
            return ""
        descpositioning = ""
        counter = sorted(counter.items(), key = lambda x: x[1], reverse=True)
        for key, value in counter:
            descpositioning += key * value
            
        res = ""
        lo, hi = 0, (len(S) - 1) // 2 + 1
        while True:
            if lo == (len(S) - 1) // 2 + 1:
                break
            res += descpositioning[lo] + descpositioning[hi] if hi < len(S) else descpositioning[lo]
            lo += 1
            hi += 1
        return res