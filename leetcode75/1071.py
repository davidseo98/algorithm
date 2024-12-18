class Solution(object):

    # Beats 100% (runtime)
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """

        len1 = len(str1)
        len2 = len(str2)
        start = min(len1, len2)
        
        while start > 0:

            if len1 % start != 0 or len2 % start != 0:
                start -= 1
                continue
            
            string = str1[:start]

            is_divisor1 = "".join(str1.split(string)) == ""
            is_divisor2 = "".join(str2.split(string)) == ""

            if is_divisor1 and is_divisor2:
                return string
            
            start -= 1

        return ""