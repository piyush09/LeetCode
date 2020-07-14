"""
Algo: Sort the intervals by their start value
      If the current interval begins after the previous interval ends, then they do not overlap and append it to the current interval to merge. Otherwise, they do overlap, and merge them by updating the end of the previous interval if it is less than the end of the current interval.

T.C. - O(NlogN) - Linear scan of the intervals list, so the runtime is due to the O(nlgn) complexity of sorting.

S.C. - O(N) - No in-place sorting done, so answer stored in 'merged' list, which would be O(N)

"""


class Solution:
    def merge(self, intervals):

        if not intervals:
            return []

        intervals.sort(key=lambda x: x[0])
        # Sorting the intervals by start time

        # Initializing merged list as empty
        merged = []
        merged.append(intervals[0])
        # Iterating through every interval in intervals list
        for interval in intervals[1:]:

            # Initially merged list is empty, so for adding first interval, taking the 'not merged' in 'if' condition
            if (merged[-1][1] < interval[
                0]):  # Comparing last merged interval's end time with current iterating interval's start time
                merged.append(interval)
            else:
                merged[-1][1] = max(merged[-1][1], interval[1])

        return merged

intervals = [[1,3],[2,6],[8,10],[15,18]]

print (Solution().merge(intervals))