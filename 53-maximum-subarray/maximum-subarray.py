class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxending = nums[0]
        res = nums[0]

        for i in range(1,len(nums)):

            maxending = max(maxending + nums[i], nums[i])
            res = max(res, maxending)

        return res