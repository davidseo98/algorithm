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
    
    # Beats 99.9% (runtime)
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """

        indices = []
        vowel_set = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}

        s = list(s)

        for i, letter in enumerate(s):
            if letter in vowel_set:
                indices.append(i)

        start, end = 0, len(indices) - 1

        # Only loops N/2
        for i in range(len(indices) // 2):
            i1, i2 = indices[start + i], indices[end-1]
            s[i1], s[i2] = s[i2], s[i1]