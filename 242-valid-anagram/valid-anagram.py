class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        charactercount = {}
           
        for ch in s: 
            charactercount[ch] = charactercount.get(ch,0) + 1
               
        for ch in t:
            charactercount[ch] = charactercount.get(ch,0) - 1
               
          
        for value in charactercount.values():
            if value != 0:
                return False
                
        return True
       