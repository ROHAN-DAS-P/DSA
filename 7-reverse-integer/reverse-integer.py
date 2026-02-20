class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        rev = 0
        
        while x != 0:
            pop = int(x % 10)
            
            # Fix for Python negative division behavior
            if x < 0 and pop > 0:
                pop -= 10
            
            x = (x - pop) // 10
            
            # Overflow check
            if rev > 214748364 or (rev == 214748364 and pop > 7):
                return 0
            if rev < -214748364 or (rev == -214748364 and pop < -8):
                return 0
            
            rev = rev * 10 + pop
        
        return rev