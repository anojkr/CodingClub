class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: if a person could attend all meetings
    """

    def can_attend_meetings(self, intervals: List[Interval]) -> bool:
        # Write your code here
        N = len(intervals)
        count = 1
        if N == 0:
            return True
        intervals.sort(key=lambda x: x.start)
        endPrev = intervals[0].end
        for i in range(1, N):
            startCurr = intervals[i].start
            if endPrev > startCurr:
                count = count + 1
                endPrev = intervals[i].end
            else:
                endPrev = intervals[i].end
        return count == 1
