class Solution(object):
    def firstMatchingIndex(self, s):
        """
        :type s: str
        :rtype: int
        """
        left = 0
        right = len(s) - 1

        while left <= right:

            if s[left] == s[right]:
                return left

            left += 1
            right -= 1

        return -1