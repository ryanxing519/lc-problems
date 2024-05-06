from typing import *


class Solution:
    def insert(
        self, intervals: List[List[int]], newInterval: List[int]
    ) -> List[List[int]]:

        # one pass, if the start of the new interval (one were trying to insert) is bigger than the current's end
        # we should append the current and continue
        # if it is not, then we need to update the interval we are trying to add
        # min of starts, max of ends and continue comparing

        new_start, new_end = newInterval[0], newInterval[1]

        ans = []

        for i in range(len(intervals)):
            start, end = intervals[i]
            if new_start > end:
                ans.append([start, end])
            elif new_end < start:
                ans.append[[new_start, new_end]]
                return ans + intervals[i:]
            else:
                new_start = min(start, new_start)
                new_end = max(end, new_end)

        ans.append([new_start, new_end])
        return ans
