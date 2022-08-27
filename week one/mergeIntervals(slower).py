class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals)< 2:
            return intervals
        intervals.sort()
        output = [intervals[0]]
        for s,e in intervals[1:]:
            if s > output[-1][1]:
                output.append([s,e])
            elif e > output[-1][1]:
                output[-1][1] = e
        return output                

