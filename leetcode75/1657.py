from collections import Counter

class Solution(object):

    # Beats 29.95%(runtime)
    def closeStrings(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: bool
        """
        letters1_set = set(word1)
        letters2_set = set(word2)

        if letters1_set != letters2_set:
            return False
        
        letters1_cnt = sorted(Counter(list(word1)).values())
        letters2_cnt = sorted(Counter(list(word2)).values())

        for l1, l2 in zip(letters1_cnt, letters2_cnt):
            if l1 != l2: return False

        return True