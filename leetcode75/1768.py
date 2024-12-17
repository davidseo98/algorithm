class Solution(object):

    # Beats 10.91% (runtime)
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """

        min_len = min(len(word1), len(word2)) # len() -> O(1), has an internal attribute that saves length 

        merged_word = ""
        for i in range(min_len): # for loop -> O(n)
            merged_word += word1[i]
            merged_word += word2[i]
        
        if len(word1) > len(word2):
            return merged_word + word1[min_len:]
        elif len(word1) < len(word2):
            return merged_word + word2[min_len:]
        else:
            return merged_word
    
    # Beats 76.48% (runtime)
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """

        merged_word = ""
        
        for w1, w2 in zip(word1, word2): # Does not access the value through indexing, Auto unpacking

            merged_word += w1
            merged_word += w2
        
        if len(word1) >= len(word2):
            return merged_word + word1[len(word2):]
        else:
            return merged_word + word2[len(word1):]
    
    # Beats 88.44% (runtime)
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """

        merged_word = ""
        
        for w1, w2 in zip(word1, word2):

            merged_word += w1
            merged_word += w2

        len_1 = len(word1) # time saved by saving length as variable and not calling the attribute everytime
        len_2 = len(word2)
        
        if len_1 >= len_2:
            return merged_word + word1[len_2:]
        else:
            return merged_word + word2[len_1:]