class Solution:
    def maxPower(self, s: str) -> int:

        maxLen = 1
        currMax = 1

        for i in range(1,len(s)): 
            if (s[i] == s[i-1]):
                currMax += 1
            else: 
                currMax = 1
            
            maxLen = max(maxLen, currMax)
        return maxLen