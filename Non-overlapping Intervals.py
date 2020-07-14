"""
Algo: Sort the intervals by their start time.
    If two intervals overlap, the interval with larger end time will be removed so as to have as little impact on subsequent intervals as possible.

T.C. - O(N log N), runtime is due to the O(nlgn) complexity of sorting
S.C. - O(1), Constant space is used.

"""
class Solution:
    def eraseOverlapIntervals(self, intervals):

        if not intervals:
            return 0

        # Sorting the intervals by start time
        intervals.sort(key=lambda x: x[0])

        currentEnd = intervals[0][1]
        count = 0  # Number of intervals to be removed

        for interval in intervals[1:]:

            if (interval[0] < currentEnd):  # Overlapping Interval
                count += 1
                currentEnd = min(currentEnd, interval[1])  # Erase the one with larger end time

            else:
                currentEnd = interval[1]  # update end time

        return count

intervals = [[1,2],[2,3],[3,4],[1,3]]
print (Solution().eraseOverlapIntervals(intervals))
