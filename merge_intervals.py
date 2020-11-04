class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) <= 1:
            return intervals
        intervals.sort(key = lambda x: x[0])
        res = []
        start, end = intervals[0]
        for interval in intervals[1:]:
            if interval[0] <= end:
                end = max(interval[1], end)
            else:
                res.append([start, end])
                start = interval[0]
                end = interval[1]
        res.append([start, end])
        return res
        
