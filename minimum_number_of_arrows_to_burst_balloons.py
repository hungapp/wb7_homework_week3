class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0
        points.sort(key = lambda p: p[1])
        arrow_last_pos = points[0][1]
        arrow_count = 1
        for p in points:
            if arrow_last_pos >= p[0]:
                continue
            arrow_count += 1
            arrow_last_pos = p[1]
        return arrow_count
