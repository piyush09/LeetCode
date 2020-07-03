# O(nlgn) time, the same as Merge Intervals
# https://leetcode.com/problems/merge-intervals/

#         intervals.append(newInterval)
#         intervals.sort(key = lambda x:x[0])
#         # Sorting the intervals by start time

#         # Initializing merged list as empty
#         merged = []
#         merged.append(intervals[0])
#         # Iterating through every interval in intervals list
#         for interval in intervals[1:]:

#             #Initially merged list is empty, so for adding first interval, taking the 'not merged' in 'if' condition
#             if (merged[-1][1] < interval[0]): # Comparing last merged interval's end time with current iterating interval's start time
#                 merged.append(interval)
#             else:
#                 merged[-1][1] = max(merged[-1][1], interval[1])

#         return merged

# O(n) time, not in-place, make use of the property that the intervals                  were initially sorted according to their start times


def insert(intervals, newInterval):

    result = []

    for index, interval in enumerate(intervals):

        # If iterating interval's end time is less than new Interval start time, just append the iterating interval in the resulting list
        if interval[1] < newInterval[0]:
            result.append(interval)

        # If New Interval's end value is less than iterating interval's start time
        elif newInterval[1] < interval[0]:
            result.append(newInterval)
            return result + intervals[
                            index:]  # can return earlier with result and adding to all these remaining intervals after the index

        else:  # overlap case

            # For overlap, new interval's min. is min. of iterating interval's min. and new interval's min.
            newInterval[0] = min(newInterval[0], interval[0])

            # For overlap, new interval's max. is max. of iterating interval's max. and new interval's max.
            newInterval[1] = max(newInterval[1], interval[1])

    # Case where new interval's start is less than all interval's end, then append it in result list
    result.append(newInterval)
    return result

# intervals = [[1,3],[6,9]]
# newInterval = [2,5]

intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
newInterval = [4,8]

print (insert(intervals, newInterval))