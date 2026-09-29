"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        # Sort meetings by their start time.
        intervals.sort(key=lambda meeting: meeting.start)

        # Compare each meeting with the one immediately before it.
        for i in range(1, len(intervals)):
            previous = intervals[i - 1]
            current = intervals[i]

            # If the previous meeting ends after the current starts,
            # the meetings overlap.
            if previous.end > current.start:
                return False

        return True

