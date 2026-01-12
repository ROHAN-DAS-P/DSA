class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals.sort()

        res = []
        res.append(intervals[0])

        for i in range(1, len(intervals)):
            last = res[-1]
            curr = intervals[i]

            # If current interval overlaps with the last merged
            # interval, merge them 
            if curr[0] <= last[1]:
                last[1] = max(last[1], curr[1])
            else:
                res.append(curr)

        return res