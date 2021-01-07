class Solution:
    def merge(self, intervals):
        if intervals is None or len(intervals) == 0:
            return
        out = []
        intervals.sort()
        
        start, end = intervals[0][0], intervals[0][1]
        
        for i in range(1, len(intervals)):
            s, e = intervals[i][0], intervals[i][1]
            if end >= s:
                end = max(e, end)
            else:
                out.append([start, end])
                start = s
                end = e
        out.append([start, end])
        return out