class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        result = []
        intervals.sort(key=lambda x: x[0])
        result.append(intervals[0])

        for i in range(1, len(intervals)):
            minA = min(result[-1])
            maxA = max(result[-1])
            minB = min(intervals[i])
            maxB = max(intervals[i])
            if maxA >= minB:
                if maxA <= maxB:
                    if (len(result) == 0):
                        result.append([min(minA, minB), max(maxA, maxB)])
                    else:
                        result.pop()
                        result.append([min(minA, minB), max(maxA, maxB)])
            else:
                result.append([minB, maxB])
        return result
