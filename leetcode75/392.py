class Solution(object):

    # beats 43% (runtime)
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if s == "": return True
        if t == "": return False
        length = len(s)
        idx = 0
        cur = s[idx]
        for letter in t:
            if letter == cur:
                idx += 1

                if idx == length:
                    return True
                cur = s[idx]

        return False