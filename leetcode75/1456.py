class Solution(object):

    # Beats 88.03% (runtime)
    def maxVowels(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        
        vowels = {"a", "e", "i", "o", "u"}

        max_cnt = 0

        for letter in s[:k]:
            if letter in vowels: max_cnt+=1

        prev_cnt = max_cnt

        for i in range(len(s)-k):

            if s[i+k] in vowels:
                prev_cnt += 1
            
            if s[i] in vowels:
                prev_cnt -= 1
            
            max_cnt = max(max_cnt, prev_cnt)

        return max_cnt
