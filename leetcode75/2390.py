class Solution(object):
    def removeStars(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        stack = []

        for letter in s:
            if s == "*":
                stack.pop()
            else:
                stack.append(letter)
        
        return "".join(stack)