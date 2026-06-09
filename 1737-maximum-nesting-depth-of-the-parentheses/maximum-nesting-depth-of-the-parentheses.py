class Solution:
    def maxDepth(self, s: str) -> int:
        current_depth = 0
        max_depth = 0

        for ch in s:
            if ch == '(':
                current_depth += 1

            elif ch == ')':
                current_depth -= 1
            
            max_depth = max(max_depth, current_depth)
        
        return max_depth