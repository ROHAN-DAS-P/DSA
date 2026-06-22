class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """


        stack = []

        mapping = {
            ')': '(',
            ']': '[',
            '}': '{'
        }

        for ch in s:

            # Opening bracket
            if ch in "([{":
                stack.append(ch)

            # Closing bracket
            else:

                if not stack:
                    return False

                if stack.pop() != mapping[ch]:
                    return False

        return not stack