class Solution(object):

    # Beats 10.91%
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """

        min_len = min(len(word1), len(word2))
        merged_word = ""
        for i in range(min_len):
            merged_word += word1[i]
            merged_word += word2[i]
        
        if len(word1) > len(word2):
            return merged_word + word1[min_len:]
        elif len(word1) < len(word2):
            return merged_word + word2[min_len:]
        else:
            return merged_word