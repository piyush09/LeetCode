"""
Algorithm: Sort the meetings by start time.
          Iterate through the meetings and check that each meeting ends before the next one starts.

T.C. - O(NlogN) - Time complexity is by sorting. Once the array is sorted, 
      only O(n) time is taken to iterate through the array and determine if there is any overlap.

S.C. - O(1) - No additional space is allocated.

Question Link: http://tiancao.me/Leetcode-Unlocked/LeetCode%20Locked/c1.6.html
"""

class Solution:
    def canAttendMeetings(self, intervals):
        
        # If no meeting, then person can attend meetings.
        if not intervals:
            return True
        
        intervals.sort(key=lambda x:x[0])
        
        for i in range(0, len(intervals)-1):
            # If meeting end time is greater than other meeting's start time, return False
            if (intervals[i][-1] > intervals[i+1][0]):
                return False
            
        return True

intervals = [[0,30],[5,10],[15,20]]
intervals = [[7,10],[2,4]]
print(Solution().canAttendMeetings(intervals))
            