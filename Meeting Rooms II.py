"""
Algorithm: Sort the meetings by start time.
          Initialize a new min-heap and add the first meeting's ending time to the heap.
          Keep track of the ending times as that keeps a check on when a meeting room will get free.
          For every meeting room check if the minimum element of the heap (room at the top of the heap) is free or not.
          If the room is free, then we extract the topmost element and add it with the ending time of the current meeting/ interval.
          If not, then we allocate a new room and add it to the heap
          After processing all the meetings, the size of the heap is equal to the number of rooms allocated.

T.C. - O(NlogN) - Time complexity is by sorting - O(NlogN). Once the array is sorted.

    In the min-heap. In the worst case, all N meetings will collide with each other. In any case, there are N add operations on the heap. 
    In the worst case, there will be N extract-min operations as well. 
    Overall complexity being (NlogN) since extract-min operation on a heap takes O(logN).

S.C. - O(N) - because we construct the min-heap and that can contain N elements in the worst case, as in TC section above.

Question Link: http://tiancao.me/Leetcode-Unlocked/LeetCode%20Locked/c1.6.html
"""

import heapq
class Solution:
    def minMeetingRooms(self, intervals):
        
        # If no meeting to schedule, then no room needs to be allocated.
        if not intervals:
            return 0

        # The heap initialization
        free_rooms = []

        # Sort the meetings in increasing order of their start time.
        intervals.sort(key= lambda x: x[0])

        # Add the first meeting, Give a new room to the first meeting.
        heapq.heappush(free_rooms, intervals[0][1])

        # For all the remaining meeting rooms
        for interval in intervals[1:]:

            # If the room due to free up the earliest is free, assign that room to this meeting.
            if free_rooms[0] <= interval[0]:
                heapq.heappop(free_rooms)

            # If a new room is to be assigned, then also add it to the heap,
            # If an old room is allocated, then also need to add to the heap with updated end time.
            heapq.heappush(free_rooms, interval[1])

        # The size of the heap tells the minimum rooms required for all the meetings.
        return len(free_rooms)
                
intervals = [[2,15],[36,45],[9,29],[16,23],[4,9]]

print ("Minimum Number of Conference rooms required are:")
print(Solution().minMeetingRooms(intervals))
        