class Solution(object):

    # Beats 70.14% (runtime)
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """

        indices = []
        vowels = []

        vowel_set = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}
        
        s = list(s)

        for i, letter in enumerate(s):
            if letter is vowel_set:
                indices.append(i)
                vowels.append(letter)

        vowels = vowels[::-1]

        for i, v in zip(indices, vowels):
            s[i] = v

        return "".join(s)
        
        