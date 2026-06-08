class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        MAX_CHAR = 26
        vis = [-1] * MAX_CHAR

        for i in range(len(s)):
            index = ord(s[i]) - ord('a')
            if vis[index] == -1:
                vis[index] = i
            else:
                vis[index] = -2

        idx = float('inf')
        for i in range(MAX_CHAR):
            if vis[i] >= 0:
                idx = min(idx, vis[i])

        return -1 if idx == float('inf') else idx