class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        sa = set(nums1)
        res = []

        for elem in nums2: 
            if elem in sa:
                res.append(elem)
                sa.remove(elem)

        return res
        